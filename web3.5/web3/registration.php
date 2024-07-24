<?php
session_start();
$host='localhost';
$username='root';
$password='';
$dbname='database1';
// Create connection
$conn = new mysqli_connect($host, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

$fname=$_POST['fname'];
$lname=$_POST['lname'];
$gname=$_POST['gmail'];
$gmail=$_POST['gname'];
$stu=$_POST['stu'];
$pass=$_POST['pass'];
$confirmpassword=$_POST['confirmpassword'];

$sql="INSERT INTO register (fname,lname,gmail,gname,stu,pass,confirmpassword) VALUES ('$fname','$lname','$gmail','$gname','$stu','$pass','$confirmpassword')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
  header("location:loginpage.html");
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>