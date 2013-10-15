<?php
$db_host = "localhost";
$db_port = 3306;
$db_name = "qq";

$db_user = "root";
$db_pawd = "root";    

$db = mysql_connect($db_host . ":" . $db_port, $db_user,$db_pawd);

if (! $db) {
    $msg = sprintf("Could not connect to : %s:%s/ <br/>Error: %s" ,$db_host,$db_port,mysql_error());
    die ($msg);
}

mysql_select_db ($db_name,$db);

?>
