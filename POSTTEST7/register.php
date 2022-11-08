<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrasi</title>
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
    <h3>Registrasi Akun</h3>
    <form action=""method="post">
        <label for="">Email</label><br>
        <input type="text"name="email"><br><br>

        <label for="">Username</label><br>
        <input type="text"name="username"><br><br>

        <label for="">Pasword</label><br>
        <input type="password"name="password"><br><br>

        <label for="">Konfirmasi password</label><br>
        <input type="password"name="konfirmasi"><br><br>

        <input type="submit" name="regis" value ="Registrasi">
    </form>

    <p>Sudah punya akun?
        <a href="login.php">Login</a>
    </p>
</body>
</html>
<?php
    require 'config.php';
    if(isset($_POST['regis'])){
        $email=$_POST['email'];
        $username=$_POST['username'];
        $password=$_POST['password'];
        $konfirmasi=$_POST['konfirmasi'];

        $user=$db->query("SELECT * FROM akun WHERE username='$username'");

        if(mysqli_num_rows($user)>0){
            echo"<script>
                alert('Username telah digunakan, silahkan gunakan username lain')
                </script>";
        }else{
            if($password==$konfirmasi){
                $password= password_hash($password, PASSWORD_DEFAULT); //bikin supaya password seperti di enkripsi 
                $query= "INSERT INTO akun
                            VALUES ('','$email', '$username', '$password')";

                $result= $db->query($query);
                if ($result){
                    echo" <script>
                            alert('Registrasi Berhasil');
                        </script>";

                }else{
                    echo" <script>
                            alert('Registrasi gagagl');
                        </script>";

                }

            }
            else{
                echo" <script>
                                alert('Registrasi gagagl');
                            </script>";
    
        }
       
        }

    }