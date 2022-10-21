<?php
    require 'config.php';

    if(isset($_GET['id'])){
        $id = $_GET['id'];

        $result = mysqli_query($db, "SELECT * FROM prodak WHERE id='$id'" );
        $row = mysqli_fetch_array($result);
        // echo $row['nama_produk'];
    }

    if(isset($_POST['submit'])){
        $nomor = $_POST['noProduk'];
        $nama = $_POST['namaProduk'];
        $jumlah = $_POST['jumlahProduk'];
        $harga = $_POST['hargaProduk'];

        $hasil = mysqli_query($db, "UPDATE prodak SET nomor_produk = '$nomor', nama_produk= '$nama', jumlah_produk = '$jumlah', harga_produk = '$harga' WHERE id = '$id'");

        if($hasil){
            echo "
                <script> alert('Data Berhasil Di tambahkan'); </script>";
                header("Location:CalisTampil.php");
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Calis</title>
    <link rel="stylesheet" href="CalistaS.css">
</head>
<body>
<div class="headerc"> 
<i><div class="header-awal2"> Calista </div></i>
        <div class="header-list2">
            <ul>
                <li>
                    <nav class="anu">
                        <b> 
                        <a href="CalistaAbout.php">About Me</a> </b>
                    </nav>
                </li>
                <li> 
                    <nav class="shop">
                        <b>
                        <a href="CalistaShop.php">Home</a>        
                        </b>
                    </nav>
                </li>
                <li>
                <nav class="shop">
                        <b>
                        <a href="CalisTampil.php">Tabel</a>        
                        </b>
                    </nav>
                </li>
            </ul>
        </div>
    </div>
    <!-- <h3> Edit Produk </h3> -->
    <div class="form-class"> 
    <form action="" method="post">
        <table style="margin-left:auto;margin-right:auto;margin-top:60px" border = "1">
        <tr>
            <th colspan = "2"><h3> EDIT PRODUK </h3></th>
        </tr>
        <tr>
            <td><label for="">Nomor Produk : </label> <br></td>
            <td><input 
                type="text" 
                name="noProduk"  
                value=<?=$row['nomor_produk']?>><br> 
            </td>
            
        </tr>

        <tr>
            <td><label for="">Nama  Produk : </label> <br> </td>
            <td><input 
            type="text" 
            name="namaProduk" 
            value="<?=$row['nama_produk']?>"><br></td>
        </tr>
            <td>
                <label for="">Jumlah  Produk : </label> <br>
            </td>
            <td>
                <input 
                type="text" 
                name="jumlahProduk"
                value="<?=$row['jumlah_produk']?>" ><br>
            </td>
        <tr> 
            <td>
                <label for="">Harga Produk : </label> <br>
            </td>
            <td>
                <input type="text" name="hargaProduk"value="<?=$row['harga_produk']?>"><br>
            </td>
        </tr>
        <tr>
            <td colspan = "4"><input type="submit" name="submit"> </td>
        </tr>
        
        </table>
    </div>
    </form>
</body>
</html>