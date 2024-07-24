<?php
session_start();
if(isset($_POST['submit']))
{
mysql_connect('localhost','root','') ;
mysql_select_db('registration') ;
$gmail=$_POST['gmail'];
$pass=$_POST['pass'];
if($gmail!=''&&$pwd!='')
{
 $query=mysql_query("select * from register where gmail='".$gmail."' and pass='".$pass."'stu='".$stu."'");
 $res=mysql_fetch_row($query);
 if($res){
    $_SESSION['gmail']=$gmail;
    if($stu=="student"){
        $command=escapeshellcmd('python Main.py');//it used to call the python code with phpSz
        $output=shell_exec($command);
    }
    else{
        $command1=escapeshellcmd('python Main1.py');
        $output1=shell_exec($command1);
        
    }
 
 }
 else
 {
 echo'You entered username or password is incorrect';
 }
}
else
{
 echo'Enter both username and password';
}
}
?>
 