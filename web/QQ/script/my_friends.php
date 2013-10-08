<?php
include 'conn.php';
include 'util.php';
include 'pubf.php';

if (! is_login())
    die (err_msg ('请先登录') );

$id = get_user();
$sql = "select * from friends,user where owner = $id and friend = uid";
$result = mysql_query ($sql, $db);
if (! $result )
    die (err_msg ('查询好友信息失败') );

$friends = array ();
$i = 0;
while ($row = mysql_fetch_array ($result)) {
    $friends[$i++] = array ('uid'=> $row['uid'], 'name'=> $row['name'], 'nickname'=> $row['nickname'], 
        'signed' => $row['signed'], 'state' => $row['state'], );
}

echo suc_msg ('操作成功', json_decode($friends));

?>



