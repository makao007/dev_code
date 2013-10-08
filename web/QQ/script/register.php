<?php
include ('conn.php');
include ('util.php');
include ('pubf.php');

if (isset($_GET['user']) and isset($_GET['pw1']) and isset($_GET['pw2']) ) {
    $user = get_header('user');
    $pw1  = get_header('pw1');
    $pw2  = get_header('pw2');
    if ($pw1 != $pw2)
        die (err_msg('密码不一致!'));
    $sex = get_header('sex');
    $email = get_header('email');
    $nickname = get_header('nickname') == "" ? $user : get_header('nickname');
    $des = get_header('description');
    $pw_md5 = md5($pw1);

    if (has_username($user))
        die (err_msg('该帐号已被注册! 请换另一个'));

    $sql1 = "insert into user (name,pawd,nickname) values ('$user','$pw_md5','$nickname')";
    $result = mysql_query($sql1,$db);
    if (! $result)
        die (err_msg('添加用户失败'));
    else {
        $max_id = mysql_fetch_row (mysql_query ("select last_insert_id() limit 1",$db));
        $max_id = $max_id[0];
        $sql2 = "insert into person_info (uid,sex,description,created) values ($max_id,'$sex','$des',now())";
        $result2 = mysql_query($sql2, $db);
        if (! $result2 )
            die (err_msg ('添加信息失败'));
        else
            echo (suc_msg('注册成功!'));
    }
} else 
    die (err_msg('用户名和密码不能为空'));

?>
