<?php

include ('conn.php');
include ('util.php');
include ('pubf.php');

if (! is_login() )
    die (err_msg ('请先登录'));

//好友的id
$f_id = get_header ('id');
$text = get_header ('text');

$user = get_user ();

if (! has_friend ($user, $f_id))
    die (err_msg ('您只能向自己的好友发送消息'));

$sql = "insert into message (type, mfrom, mto, content, created ) values ('u', $user, $f_id, '$text', now() )";

$result = mysql_query ($sql, $db);
if (! $result)
    die (err_msg ('发送消息失败' . mysql_error()));

echo (suc_msg ('操作成功'));

?>

