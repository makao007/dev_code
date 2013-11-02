<?php 
include ("conn.php");
include ("util.php");
if (! is_login())
    die ( err_msg ('请先登录!') );

$id = get_header('id');

if (! $id) 
    die (err_msg('帐号不能为空'));

$sql = "select * from user,person_info where name='$id' and user.uid=person_info.uid";
$result = mysql_query($sql,$db);
if (! $result)
    die ("{status:0, text: '查询用户信息失败'}");
$row = mysql_fetch_array($result);
if (! $row )
    die (err_msg('没有该用户'));

$info = array ('name'=>$row['name'], 'nickname'=> $row['nickname'], 'description'=> $row['description'], 
    'sex'=> $row['sex'],'id'=> $row['uid'] );

echo "{status:1, text: " . json_encode($info) . "}";

?>


