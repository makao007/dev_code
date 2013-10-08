<?php
include ("conn.php");
include ("util.php");
include ("pubf.php");

$f_id = get_header ("f_id");
$msg  = get_header ("msg");

if ( $f_id == '')
    die (err_msg('好友的帐号不能为空'));

if (is_login()) {
    $user = get_user();
    $row = has_username($f_id);
    if (! $row )
        die (err_msg ("不存在帐号为: $f_id 的用户"));
    else {
        $id = $row['uid'];
        if ($id == $user )
            die (err_msg ('你不能加自己为好友!'));
        else {
            if (has_friend($user, $id))
                die (err_msg('他（她）已是您的好友!'));
            $nickname = $row['nickname'];
            $msg = "$f_id($nickname) 请求添加您为好友 // $msg" ; 
            $sql2 = "insert into message (type,mfrom,mto, content, created ) values ('f','$user','$id', '$msg', now() ) ";
            $result2 = mysql_query($sql2,$db);
            if (! $result2)
                die (err_msg ("插入消息失败" . mysql_error()));
            else 
                echo (suc_msg('已发送添加好友请求'));
        }
    }
} else {
    die (err_msg('请先登录!'));
}

