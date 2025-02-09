import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from skimage.feature import graycomatrix, graycoprops
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer


def calculate_eccentricity(contour):
    if len(contour) >= 5:  # Perlu minimal 5 titik untuk fitEllipse
        ellipse = cv2.fitEllipse(contour)
        major_axis = max(ellipse[1])  # Sumbu utama
        minor_axis = min(ellipse[1])  # Sumbu minor
        eccentricity = np.sqrt(1 - (minor_axis ** 2 / major_axis ** 2))
        return eccentricity
    else:
        return None

# Fungsi untuk menghitung metric (roundness)
def calculate_metric(contour):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if perimeter > 0:
        metric = (4 * np.pi * area) / (perimeter ** 2)
        return metric
    else:
        return None


def extract(image_path):
    image = cv2.imread(image_path) #Baca Gambar
    resized_image = cv2.resize(image, (300, 300)) #Resize

    #crop
    height, width = resized_image.shape[:2]
    start_x, start_y = width // 4, height // 4
    end_x, end_y = start_x + (width // 2), start_y + (height // 2)
    cropped_image = resized_image[start_y:end_y, start_x:end_x]

    #Crop > Grayscale
    cropped_gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    #--- Fitur ----
    #Warna 
    mean_intensity = np.mean(cropped_gray)
    std_intensity = np.std(cropped_gray)
    
    #Glcm (Tekstur)
    glcm = graycomatrix(cropped_gray, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]

    #Bentuk
    _, otsu_threshold = cv2.threshold(cropped_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
 
    #Temukan kontur pada gambar hasil thresholding
    contours, _ = cv2.findContours(otsu_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   
    # Analisis eccentricity dan metric untuk setiap kontur (Bentuk)
    eccentricities = []
    metrics = []

    for contour in contours:
        ecc = calculate_eccentricity(contour)
        metric = calculate_metric(contour)

        if ecc is not None:
            eccentricities.append(ecc)
        if metric is not None:
            metrics.append(metric)

    avg_eccentricity = np.mean(eccentricities) if eccentricities else 0
    avg_metric = np.mean(metrics) if metrics else 0 

    # Gabungkan semua fitur
    features = [mean_intensity, std_intensity, contrast, correlation, energy, homogeneity,avg_eccentricity,avg_metric]
    return features

def load_dataset(base_path):
    """Load dataset dari folder"""
    features = []
    labels = []
    
    # Iterasi setiap folder kelas
    for class_name in os.listdir(base_path):
        class_path = os.path.join(base_path, class_name)
        if os.path.isdir(class_path):
            # Iterasi setiap gambar dalam folder kelas
            for image_name in os.listdir(class_path):
                if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(class_path, image_name)
                    try:
                        # Ekstrak fitur dari gambar
                        image_features = extract(image_path)
                        features.append(image_features)
                        labels.append(class_name)
                    except Exception as e:
                        print(f"Error processing {image_path}: {str(e)}")
    
    return np.array(features), np.array(labels)

def train_and_evaluate_model():
    #loksi dataset
    dataset_path = r"D:\! Code\Klasifikasi\dataset"

    #dataset
    print("Loading dataset...")
    features, labels = load_dataset(dataset_path)

#-------------------------------------------------------------------------
    #NgeCek Data Set Kebaca Atau Ngga
    if len(features) ==0:
        print("Kosong")
        
        return None,None
    print(f"Total data: {len(features)} samples")
    print(f"Label unik: {set(labels)}") 
#-------------------------------------------------------------------------
    
    print("Memeriksa nilai NaN dalam dataset...")
    print(f"Total nilai NaN: {np.isnan(features).sum()}")  # Hitung total NaN
    # Hapus baris dengan NaN
    features = np.array(features)
    labels = np.array(labels)

    mask = ~np.isnan(features).any(axis=1)  # Pilih baris yang tidak mengandung NaN
    features = features[mask]
    labels = labels[mask]

    print(f"Dataset setelah menghapus NaN: {len(features)} samples")


#-------------------------------------------------------------------------


    # Normalisasi fitur
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Split dataset menjadi training dan testing
    X_train, X_test, y_train, y_test = train_test_split(
        features_scaled, labels, test_size=0.2, random_state=42)
    
     # Model KNN dengan Manhattan Distance
    knn_manhattan = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
    knn_manhattan.fit(X_train, y_train)
    acc_manhattan = knn_manhattan.score(X_test, y_test)

    # Model KNN dengan Euclidean Distance
    knn_euclidean = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
    knn_euclidean.fit(X_train, y_train)
    acc_euclidean = knn_euclidean.score(X_test, y_test)

    # Model KNN dengan Minkowski Distance (p=3)
    knn_minkowski = KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=3)
    knn_minkowski.fit(X_train, y_train)
    acc_minkowski = knn_minkowski.score(X_test, y_test)


    # Train model KNN
    print("Training KNN model...")
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    # Evaluasi model
    train_accuracy = knn.score(X_train, y_train)
    test_accuracy = knn.score(X_test, y_test)
    
    print(f"Training Accuracy: {train_accuracy:.2f}")
    print(f"Testing Accuracy: {test_accuracy:.2f}")
    
    # Cetak hasil akurasi masing-masing metode jarak
    print(f"Akurasi Manhattan Distance: {acc_manhattan:.2f}")
    print(f"Akurasi Euclidean Distance: {acc_euclidean:.2f}")
    print(f"Akurasi Minkowski Distance: {acc_minkowski:.2f}")

    # Pilih model terbaik berdasarkan akurasi tertinggi
    best_model = max(
        [(knn_manhattan, acc_manhattan),
         (knn_euclidean, acc_euclidean),
         (knn_minkowski, acc_minkowski)],
        key=lambda x: x[1]
    )[0]


    return knn, scaler , best_model , test_accuracy


def predict_single_image(model, scaler, image_path):
    """Prediksi kelas untuk satu gambar"""
    # Ekstrak fitur
    features = extract(image_path)

    print(f"Memprediksi gambar: {image_path}")
    print("Fitur yang diekstrak:", features)
    # Normalisasi fitur
    features_scaled = scaler.transform([features])
    
    # Prediksi
    prediction = model.predict(features_scaled)
    print("Hasil prediksi:", prediction[0])
    return prediction[0]


# Main program
if __name__ == "__main__":
    # Train model
    model, scaler , best_model, test_accuracy  = train_and_evaluate_model()
    
    # Prediksi gambar baru
    while True:
        # Pilih file gambar
        root = Tk()
        root.withdraw()
        image_path = filedialog.askopenfilename(
            filetypes=[("Image Files", ".jpg;.png;*.jpeg")]
        )
        
        if not image_path:
            print ("No Data Left")
            break
            
        print(f"File yang dipilih: {image_path}")  # Debugging

        # Prediksi kelas gambar
        predicted_class = predict_single_image(model, scaler, image_path)
        print(f"Predicted class: {predicted_class}")
        #lanjut = input("Ingin memprediksi gambar lain? (y/n): ").lower()
       # if lanjut != 'y':
       #     print("Program selesai.")
     #       break