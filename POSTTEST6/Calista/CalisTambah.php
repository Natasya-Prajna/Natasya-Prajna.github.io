<?php 

require 'config.php';

if(isset($_POST['submit'])){
    $nomor = $_POST['noProduk'];
    $nama = $_POST['namaProduk'];
    $jumlah = $_POST['jumlahProduk'];
    $harga = $_POST['hargaProduk'];

    $kirim = mysqli_query($db, "INSERT INTO prodak (nomor_produk,nama_produk,jumlah_produk,harga_produk) VALUES ('$nomor','$nama','$jumlah','$harga')");

    if($kirim){
        echo "<script> alert('Data Berhasil Dikirim');</script>";
        header("Location:CalisTampil.php");
    }else {
        echo "gagal mengirim";
    }
}