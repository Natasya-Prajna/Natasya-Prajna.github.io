<?php 
    require 'config.php';
    if(isset($_POST['submit'])){
        $nomor = $_POST['noProduk'];
        $nama = $_POST['namaProduk'];
        $jumlah = $_POST['jumlahProduk'];
        $harga = $_POST['hargaProduk'];

        $result = mysqli_query($db, "INSERT INTO prodak (nomor_produk,nama_produk,jumlah_produk,harga_produk) VALUES ('$nomor','$nama','$jumlah','$harga')");
        if($result){
            echo "<script> alert('Data Berhasil Di tambahkan'); </script> ";
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
    <title>Tabel Calis</title>
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
<!-- <h3> Pendaftaran Barang </h3> -->
<table style="margin-left:auto;margin-right:auto;margin-top:60px" border = "2" >
    <tr>
        <th> 
            <h3> Pendaftaran Barang </h3>
        </th>
    </tr>
        <tr>
        <td>
    <form action="" method="post">
        <label for="">Nomor Produk : </label> 
        <input type="text" name="noProduk"><br><br>
        <label for="">Nama  Produk : </label> 
        <input type="text" name="namaProduk"><br><br>
        <label for="">Jumlah  Produk : </label> 
        <input type="text" name="jumlahProduk"><br><br>
        <label for="">Harga Produk : </label> 
        <input type="text" name="hargaProduk"><br><br>

        <input type="submit" name="submit"> 
    </form>
    </tr>
    </td>
    </table>
</body>
</html>