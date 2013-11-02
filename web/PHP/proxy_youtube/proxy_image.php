<?php 

include ("common.php");
include ("conn.php");
if (! isset($_GET['url'])){
 if (! isset($_GET['url_jpg']))
  return ;
}

if (isset($_GET['url']))
 $url = $_GET['url'];
else
 $url = substr($_GET['url_jpg'],0,-4);
$url = base64_decode(strrev($url));


$result = mysql_query("SELECT content FROM images where url='$url'",$db);
if (!$result)
    mdie(mysql_error());
if (mysql_num_rows($result)==0){
    if (function_exists("file_get_contents"))
        $content = url_fetch_3($url);
    else if(function_exists("curl_init"))
        $content = url_fetch_1($url);
    else
        die("fetch url Error");
    $content2 = mysql_escape_string($content);
    $insert = mysql_query("insert into $db_table_image (url,content) values ('$url','$content2')" );
    mysql_close($db);
    if(! $insert){
        mysql_close($db);
        die(mysql_error());
    }
} else {
    $row = mysql_fetch_row($result);
    $content = $row[0];
    mysql_close($db);
}

@header("Content-Type: image/jpeg");
@header("Cache-Control: max-age = 100");
echo $content;
?>
