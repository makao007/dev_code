<?php

include ("conn.php");
include ("util.php");

if (! is_login() ) 
    die (err_msg ("请先登录"));

$user = get_user();
$sql = "select * from message where mto = $user and readed = 'n'";
$result = mysql_query ($sql, $db);
if (! $result)
    die (err_msg ("查询消息失败"));
$i = 0;
$info = array();
while ($row = mysql_fetch_array ($result))
    $info[$i++] = array ('mid'=>$row['mid'], 'type'=> $row['type'], 'mfrom'=>$row['mfrom'], 'content'=> $row['content'] , 'created'=> $row['created'] );

if (! $info)
    die (err_msg ('记录为空') );

echo suc_msg ('',json_encode($info));

if (! $info)
    return;
$sql2 = "update message set readed = 'y' where mto = $user and readed='n'";
$result2 = mysql_query ($sql2, $db);
if (! $result2) 
    die (err_msg ("修改消息失败"));

?>
