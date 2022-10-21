<?php
    require 'config.php';
    $result = mysqli_query($db, "SELECT * FROM prodak");

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="CalistaS.css">
    <title>Tabel</title>
</head>
<body>
<div class="Header">
        <i><div class="header-awal"> Calista 
        </div></i>
        <div class="header-list">
            <ul>
                <li> <a href="CalistaAbout.php">About Me</a> </li>
                <li> <a href="CalistaShop.php">Home</a></li>  
                <li> <a href="CalisTampil.php"> Tabel </a></li>
            </ul>
        </div>
    </div>
<!-- <h3> Daftar Produk Baru : </h3> -->
        <table style="margin-left:auto;margin-right:auto;margin-top:10px" border="2">
            <tr>
                <th colspan = "9">
                    <h2>DAFTAR PRODUK : </h2>
                </th>
            </tr>
            <tr>
                <th> No </th>
                <th> Nomor Produk </th>
                <th> Nama Produk </th>
                <th> Jumlah Produk </th>
                <th> Harga Produk </th>
                <th colspan="4"> Action</th>
            </tr>
            <?php
                require 'config.php';
                $i= 1;
                while($row = mysqli_fetch_array($result)){  
                    
                ?>

            <tr>
                <td> <?=$i ?></td>
                <td> <?=$row['nomor_produk']?></td>
                <td> <?=$row['nama_produk']?></td>
                <td> <?=$row['jumlah_produk']?></td>
                <td> <?=$row['harga_produk']?></td>
                <td><a href="CalissForm.php">tambah</a></td>
                <td><a href="CalisEdit.php?id=<?=$row['id']?>">edit</a></td>
                <td><a href="CalisHapus.php?id=<?=$row['id']?>">hapus</a></td>
            </tr>
            <?php 
                $i++;
                }
            ?>
        </table>
</body>
</html>