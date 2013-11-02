<?php
include ("conn.php");
include ("util.php");
$user = get_header("username");
$stat = get_header("status");
$pawd = md5(get_header("password"));

$sql = "select * from user where name='$user' and pawd='$pawd'";
$result = mysql_query($sql,$db);
if (! $result)
    die (err_msg('用户登录，查询数据库出错'));
else { 
    $row = mysql_fetch_array($result);
    if (!$row)
        die (err_msg('用户名或密码错误'));
    else {
        @session_start();
        $_SESSION['id'] = $row['uid'];
        $_SESSION['username'] = $row['name'];
        echo (suc_msg("登录成功!"));
    }
}
    

?>
