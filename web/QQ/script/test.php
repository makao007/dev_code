<?php
$a = array('a'=>1,'b'=>2,'c'=>3);
@session_start();

$b  = array();
$b[0] = array('a'=>1,'b'=>2);
$b[1] = array('a'=>1,'b'=>2);
$b[2] = array('a'=>1,'b'=>2);

include ("conn.php");
include ("util.php");
utf8();
$row = mysql_fetch_array (mysql_query ("select * from user ", $db));
echo "<br><br>";
var_dump($row);
echo "<br><br>";
echo $row['nickname'];
    /*
$a = 1;
$b = 0;
echo "<br/>";
if ($a)
    echo "a yes";
else
    echo "a no";

echo "<br/>";
if (! $b)
    echo "b no";
else
    echo "b yes";
     */

?>
