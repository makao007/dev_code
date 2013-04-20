<?php
include ('conn.php');
include ('util.php');
include ('pubf.php');

if (! is_login() )
    die (err_msg ('请先登录'));

$uid = get_user();
$fid = get_header('fid');

if (! has_friend ($uid,$fid))
    die (err_msg ('您俩不是好友'));

$sql_1 = "delete from friends where owner = $uid and friend=$fid";
$sql_2 = "delete from friends where owner = $fid and friend=$uid";

function do ($s) {
    $result = mysql_query ($s, $db);
    if (! $result)
        die (err_msg ('删除失败' . mysql_error() ));
    else
        echo (suc_msg('删除成功'));
}

do ($sql_1);
do ($sql_2);

?>


