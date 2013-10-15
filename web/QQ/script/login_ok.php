<?php
include ("conn.php");
include ("util.php");

if (! is_login())
    die (err_msg('请先登录'));

$info = array ();
$user = get_user();

$sql1 = "select * from user where uid='$user'";
$result = mysql_query ($sql1,$db);
if (! $result)
    die (err_msg('获取用户信息失败'));
$row = mysql_fetch_array ($result);
if (! $row )
    die (err_msg("不存在该用户: $user !"));

//用户信息
$info['uid'] = $row['uid'];
$info['name'] = $row['name'];
$info['nickname'] = $row['nickname'];
$info['status'] = $row['state'];
$info['signed'] = $row['signed'];

$sql2 = "select * from friends,user where owner='$user' and friend=uid ";
$result2 = mysql_query ($sql2,$db);
if (! $result2)
    die (err_msg('取好友信息失败'));
$i = 0;
$info['friends'] = array();
while ( ($row = mysql_fetch_array($result2))) {
    $info['friends'][$i++] = array('nickname'=> $row['nickname'],'name'=> $row['name'], 
        'status'=> $row['state'], 'signed'=> $row['signed'], 'category'=> $row['category'],
        'uid' => $row['uid'] );
}

$sql3 = "select * from zone,zone_member where uid='$user' and zone.zid=zone_member.zid";
$result3 = mysql_query($sql3,$db);
if (! $result3)
    die (err_msg('获取群信息失败'));
$j = 0;
while ( ($row = mysql_fetch_array($result3))) {
    $info['zones'][$j++] = array ('name'=> $row['zone.name'], 'desc'=> $row['description'], 
        'msg'=> $row['msg'] );
}

echo suc_msg ('操作成功', json_encode($info) );

?>
