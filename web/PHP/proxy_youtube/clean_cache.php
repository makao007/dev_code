<?php
include ("conn.php");
$result = mysql_query("delete from $db_table_image",$db);
if(!$result)
    die("delete records from table $db_table_image error". mysql_error());

$result = mysql_query("delete from $db_table_xml",$db);
if(!$result)
    die("delete records from table $db_table_xml error". mysql_error());

?>


