<?php
session_start();
$host='localhost';
$username='root';
$password='';
$dbname='database1';
$conn=mysqli_connect($host,$username,$password,$dbname);

$fname=$_POST['fname'];
$lname=$_POST['lname'];
$gname=$_POST['gname'];
$gmail=$_POST['gmail'];
$stu=$_POST['stu'];
$pass=$_POST['pass'];
$confirmpassword=$_POST['confirmpassword'];

$sql="insert into register(fname,lanem,gname,gmail,stu,pass,confirmpassword) 
values('$fname','$lname','$gname','$gmail','$stu',$pass','$confirmpassword')";
$s=mysqli_select_db($dbname,$sql);
$retval=mysqli_query($sql,$s);
if(!$retval )
{
die('Could not enter data: ' . mysqli_error($conn,$sql));
//die('Your Data is not Registered');
//echo'<script> alert("Your Data is not Registered")</script>';
  
}
else{

header("Location: loginpage.html");
mysqli_close($conn,$sql);
}
?>