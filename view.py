import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from skimage.feature import graycomatrix, graycoprops
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Fungsi untuk memilih file gambar
def select_image():
    root = Tk()
    root.withdraw()  # Menyembunyikan jendela utama
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    return file_path

# Fungsi untuk menghitung eccentricity
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

# Fungsi untuk menghitung GLCM fitur
def calculate_glcm_features(image):
    glcm = graycomatrix(image, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    return contrast, correlation, energy, homogeneity

# Pilih file gambar
image_path = select_image()

if image_path:  # Jika pengguna memilih file
    # Baca gambar
    image = cv2.imread(image_path)

    # Resize gambar (ubah ukuran ke 300x300 piksel)
    resized_image = cv2.resize(image, (300, 300))

    # Crop bagian tengah gambar
    height, width = resized_image.shape[:2]
    start_x, start_y = width // 4, height // 4
    end_x, end_y = start_x + (width // 2), start_y + (height // 2)
    cropped_image = resized_image[start_y:end_y, start_x:end_x]

    # Konversi gambar crop ke grayscale untuk metode Otsu
    cropped_gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Terapkan metode Otsu
    otsu_thresh, otsu_threshold = cv2.threshold(cropped_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Hitung mean dan standard deviation (Warna)
    mean_intensity = np.mean(cropped_gray)
    std_intensity = np.std(cropped_gray)

    # Temukan kontur pada gambar hasil thresholding
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

    # Ekstraksi fitur tekstur dengan GLCM (Tekstur)
    glcm_features = calculate_glcm_features(cropped_gray)
    contrast, correlation, energy, homogeneity = glcm_features

    # Tampilkan hasil
    plt.figure(figsize=(15, 5))

    # Gambar asli
    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Gambar Asli")
    plt.axis("off")

    # Gambar resize
    plt.subplot(1, 4, 2)
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.title("Gambar Resize (300x300)")
    plt.axis("off")

    # Gambar crop (bagian tengah)
    plt.subplot(1, 4, 3)
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.title("Gambar Crop (Bagian Tengah)")
    plt.axis("off")

    # Hasil metode Otsu
    plt.subplot(1, 4, 4)
    plt.imshow(otsu_threshold, cmap='gray')
    plt.title(f"Metode Otsu (Threshold={otsu_thresh:.2f})")
    plt.axis("off")

    plt.show()

    # Tampilkan hasil fitur
    print("Mean Intensity:", mean_intensity)
    print("Standard Deviation:", std_intensity)
    print("Eccentricity:", eccentricities)
    print("Metric (Roundness):", metrics)
    print("GLCM Features:")
    print("  Contrast:", contrast)
    print("  Correlation:", correlation)
    print("  Energy:", energy)
    print("  Homogeneity:", homogeneity)

    # Persiapkan data untuk klasifikasi KNN
    features = [mean_intensity, std_intensity, contrast, correlation, energy, homogeneity]
    labels = ["Class 1"]  # Contoh label, tambahkan sesuai dataset Anda

    # Normalisasi fitur
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform([features])


    # Contoh implementasi KNN
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    X_train = np.array([...])  # Tambahkan lebih banyak data
    y_train = np.array([...])
    knn.fit(X_train, y_train)

    knn.fit(features_scaled, labels)  # Data latihan harus ditambahkan sesuai dataset
    

    prediction = knn.predict(features_scaled)  # Prediksi label
    print("Prediksi Klasifikasi:", prediction)

    
else:
    print("Tidak ada gambar yang dipilih.")
