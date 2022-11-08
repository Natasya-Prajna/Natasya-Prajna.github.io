<?php 

require 'config.php';

if(isset($_GET['id'])){
    $id = $_GET['id'];
    $hapus = mysqli_query($db, "DELETE FROM prodak WHERE id='$id'");

    if($hapus){
        header("Location:CalisTampil.php");
        echo'<script> alert ("Data Terhapus");</script>';
    }
}?>

