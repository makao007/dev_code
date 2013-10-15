<?php
include ('conn.php');
include ('util.php');
include ('pubf.php');

if (! is_login() )
    die (err_msg ('请先登录'));

$user = get_user();
$f_id = get_header('f_id');
$f_ok = get_header('f_ok');

$friend = has_user($f_id);   // friend id

if (! $friend)
    die (err_msg ("不存在该用户 $f_id "));

if (has_friend($user,$f_id))
    dir (err_msg ('他（她）已是您的好友！'));

if ($f_ok == 'y') {
    $sql_1 = "insert into friends (owner,friend,created) values ('$user','$f_id',now())";
    $result = mysql_query($sql_1, $db);
    if (! $result)
        die (err_msg ('添加好友，插入数据库失败'));

    $sql_2 = "insert into friends (owner,friend,created) values ('$f_id','$user',now())";
    $result_2 = mysql_query ($sql_2, $db);
    if (! $result_2)
        die (err_msg ('添加好友，插入数据库失败'));

    $msg = sprintf ("%s(%s) 同意添加您为好友",$friend['name'] ,$friend['nickname'] ); 
    $sql_3 = "insert into message (type,mfrom,mto,content,created) values ('s',$user,$f_id,'$msg', now()) ";
    $result_3 = mysql_query ($sql_3,$db);
    if (! $result_3 )
        die (err_msg('添加好友，插入消息失败'));
    echo (suc_msg (sprintf("成功添加好友 %s(%s)",$friend['name'],$friend['nickname']), json_encode($friend)));

}  else if ($f_ok == 'n') {

    $msg = sprintf("%s(%s) 拒绝添加您为好友", $friend['name'], $friend['nickname']) ;
    $sql_4 = "insert into message (type,mfrom,mto,content,created) values ('s',$user,$f_id,'$msg',now()) ";
    $result_4 = mysql_query ($sql_4, $db);
    if (! $result_4)
        die (err_msg ('添加好友，插入消息失败'));
    echo (suc_msg ('操作成功'));
}  else 
    die (err_msg ('未知操作'));


?>










