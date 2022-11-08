<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOGIN</title>
    <link rel="stylesheet" href="CalistaS.css">

    <style>
    th {
        border-radius: 5px;
        background-color: #96D4D4;
        /* border-collapse: collapse; */
    }
    tr, td {
        border-radius: 5px;
        background-color: pink;
    }
</style>
</head>
<body>
<div class="headerc"> 
        <i><div class="header-awal2"> Calista Login</div></i>

    </div>
    <form action=""method="post">
    <table style="margin-left:auto;margin-right:auto;margin-top:60px" >
        <tr>
            <th colspan="4"> 
            <h3>Login Akun</h3>
            </th>
        </tr>
        <tr>
            <td colspan="2"><label for="">Username / Email</label><br></td>
            <td ><input type="text" name="user"><br></td>
        </tr>
        <tr>
            <td colspan="2"> <label for="">Password</label><br> </td>
            <td><input type="password" name="password"><br></td>
        </tr>
        <tr>
            <td colspan="4" >
            <input type="submit" name="login" value ="login">
            </td>
        </tr>
    </form>
    <td colspan="4"> 
        <p>Belum Punya Akun?
        <a href="register.php">Register</a>
    </p></td>
    </table>
</body>
</html>

    <?php
    require 'config.php';

    session_start();
    if(isset($_POST['login'])){
        $user = $_POST['user'];
        $password = $_POST['password'];

        $query= "SELECT * FROM akun WHERE username= '$user' OR email='$user'";
        $result = mysqli_query($db,$query);
        
        // $result = $db->query($query);
        // $row =mysqli_fetch_array($result);

        if ($result->num_rows > 0) {
            $row = mysqli_fetch_assoc($result);
            $_SESSION['username'] = $row['username'];
            header("Location: CalistaShop.php");
            echo"<script>
                    alert('Selamat Datang');
                    </script>";
            
        }else {
            echo"<script>
                    alert('Username Dan Password salah');
                    </script>";
        }
    }