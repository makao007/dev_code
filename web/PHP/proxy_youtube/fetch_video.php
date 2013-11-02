<?php

include ("common.php");
@header("Content-Disposition:filename=videofeed.flv");
@header("Content-Type: video/x-flv");
@header("Pragma: no-cache");

$v = $_GET['v'];
$filename = 'http://www.youtube.com/watch?v=' . $v;
$filename = trim($filename);
$filename = str_replace(".flv","",$filename);

$default_video = 'v.flv';

$content = url_fetch_page($filename);

preg_match_all('/34\|(http:\\\\\/\\\\\/[^,|]+),/imsU',$content,$aa);

if (sizeof($aa[1])>0){
  $video_url = $aa[1];
} 
else{
  preg_match_all('/5\|(http:\\\\\/\\\\\/[^,|]+),/imsU',$content,$bb);
  if (sizeof($bb[1]) > 0)
    $video_url = $bb[1];
  else{
    preg_match_all('/18\|(http:\\\\\/\\\\\/[^,|]+),/imsU',$content,$cc);
    if (sizeof($cc[1]) > 0)
      $video_url = $cc[1];
    else
      $video_url = $default_video;
  }
}  
  
$bb = str_replace("\/",'/',$video_url[1]);
$bb = str_replace('\n','',$bb);
$bb = str_replace('\r','',$bb);
$bb = str_replace('\\u0026','&',$bb); 
url_fetch_video($bb);
?>
