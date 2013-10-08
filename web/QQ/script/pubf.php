<?php 
include ('conn.php');

function has_friend($f1,$f2) {
    global $db;
    $sql = "select * from friends where owner = $f1 and friend = $f2 limit 1";
    if (mysql_fetch_row(mysql_query ($sql, $db)))
        return 1;
    else
        return 0;
}

function has_user ($id) {
    global $db;
    $sql = "select * from user where uid = $id limit 1";
    return (mysql_fetch_array(mysql_query($sql, $db)));
}

function has_username ($name) {
    global $db;
    $sql = "select * from user where name = '$name' limit 1";
    $result = mysql_query ($sql, $db);
    return (mysql_fetch_array ($result));
    //return (mysql_fetch_array(mysql_query($sql, $db)));
}

has_friend(1,2);
?>
