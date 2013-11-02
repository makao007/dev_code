<?php
$max_result = 10;

function proxy_image($filename){
    $proxy_path = './proxy_image.php?url='.strrev(trim(base64_encode($filename)));
    return $proxy_path;
}

function url_fetch_video($file_path){
    $freadtimes=0;
    $file = fopen($file_path,"rb"); 
    @stream_set_blocking($file, 0);
    if ($file) {
        while((!feof($file)) & (0==connection_status())) {
            $tttt=fread($file,"10240");
            echo $tttt;
            @ob_flush();
            @flush();
            @usleep(60);
            $freadtimes++;
            if ($freadtimes > 30000){
                break;
            }
        }
        fclose($file);
    }
}

function url_fetch_page($file_path){
    if (function_exists("file_get_contents"))
        return url_fetch_3($file_path);
    else {
        if (function_exists("fopen"))
            return url_fetch_2($file_path);
        else{
            if (function_exists("curl_init"))
                return url_fetch_1($file_path);
            else
                return "<h2>could not download page with fopen() or curl</h2>";
        }
    }
}

function exist_xml($url){
    include ('conn.php');
    $cache_time = 3600;     //cache xml file time (seconds)
    if (!$db) die("connect db Error" . mysql_error());
    mysql_query("SET NAMES utf8"); 
    $result = mysql_query("SELECT content,fetch_time FROM xml where url='$url'",$db);
    if (!$result)
        die(mysql_error());
    $row = mysql_fetch_row($result);
    $is_expire = mysql_num_rows($result)==0? true : (strtotime(date("Y-m-d h:i:s"))-strtotime($row[1])) > $cache_time ? true:false;
    if ($is_expire){
        $delete = mysql_query("delete from $db_table_xml where url='$url'");
        if(! $delete)
            die("delete record from $db_table_xml error");
        $content = url_fetch_page($url);
        $content1 = addslashes($content);
        $insert = mysql_query("insert into $db_table_xml (url,content) values ('$url','$content1')");
        mysql_close($db);
        if(! $insert){
            die(mysql_error());
        }
    } else {
        $content = ($row[0]);
        mysql_close($db);
    }
    return stripslashes($content);
}

function xml_fetch($feedURL){
    if(function_exists('simplexml_load_string'))
        return simplexml_load_string(exist_xml($feedURL));
    if(function_exists("simplexml_load_file"))
        return simplexml_load_file($feedURL);
    else
        die('simplexml_load_string and simplexml_load_file function do not work!');
}

function url_fetch_3($file_path){
    return file_get_contents($file_path);
}

function url_fetch_2($url){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
    curl_setopt($ch, CURLOPT_TIMEOUT, 120);
    curl_setopt($ch, CURLOPT_MAXREDIRS, 5);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    @curl_setopt($ch, CURLOPT_FOLLOWLOCATION , true);
    return curl_exec($ch);
}

function url_fetch_1($file_path){
    $max_size = 2000*1024;
    $file = fopen($file_path,"rb");
    $content = fread($file,$max_size);
    fclose($file);
    return $content;
}

function make_url(){
    $url = 'http://gdata.youtube.com/feeds/api/standardfeeds/';
    if (isset($_GET['term']))
        $url = $url . "US/";
    if (isset($_GET['type']))
        $url = $url . $GET['type'];
    else
        $url = $url . 'most_viewed';
    if (isset($_GET['term']))
        $url = $url . '_' . $_GET['term'];
    if (isset($_GET['time']))
        $url = $url . '?time=' . $_GET['time'];
    else
        $url = $url . '?time=today';
    if (isset($_GET['max-results'])){
        $max_result = $_GET['max-results'];
        $url = $url . '&max-results=' . $_GET['max-results'];
    }
    else{
        $max_result = 15;
        $url = $url . '&max-results=15' ; 
    }
    if (isset($_GET['start-index']))
        $url = $url . '&start-index=' . (strval($_GET['start-index'])*$max_result);
    else
        $url = $url . '&start-index=1';
    return $url;
}

function get_video_xml($feedURL){
    $sxml =  xml_fetch($feedURL);
    $video_info = array();
    $video_count=0;
    foreach ($sxml->entry as $entry) {
      $media = $entry->children('http://search.yahoo.com/mrss/');
      
      $attrs = $media->group->player->attributes();
      $watch = $attrs['url']; 
      
      preg_match_all('/\??v=([^&]+)&?/is',$watch,$url);

      $attrs = $media->group->category->attributes();
      $category = $attrs['label'];

      $attrs = $media->group->category->attributes();
      $termm = $media->group->category;

      $attrs = $media->group->thumbnail[0]->attributes();
      $thumbnail = $attrs['url']; 

      $description = $media->group->description;
            
      $yt = $media->children('http://gdata.youtube.com/schemas/2007');
      $attrs = $yt->duration->attributes();
      $length = $attrs['seconds']; 

      $published = $entry->published;
      $updated = $entry->updated;

      $yt = $entry->children('http://gdata.youtube.com/schemas/2007');
      if ($yt->statistics){
        $attrs = $yt->statistics->attributes();
        $viewCount = $attrs['viewCount']; 
      } else{
          $viewCount = 0;
      }
      $gd = $entry->children('http://schemas.google.com/g/2005'); 
      if ($gd->rating) {
         $attrs = $gd->rating->attributes();
         $rating = $attrs['average']; 
      } else {
         $rating = 0; 
      }
      $video_info[$video_count] = array($media->group->title,$entry->author->name,$watch,$category,$termm,$thumbnail,$length,$viewCount,$rating,$description,$url[1][0],$published,$updated);
      $video_count ++;
    }
    return $video_info; 
}

function get_search_video_xml($feedURL){
      $sxml =  xml_fetch($feedURL);
      $counts = $sxml->children('http://a9.com/-/spec/opensearchrss/1.0/');
      $total = $counts->totalResults; 
      $startOffset = $counts->startIndex; 
      $endOffset = ($startOffset-1) + $counts->itemsPerPage;       
      $video_info = array();
      $video_count = 0;
      foreach ($sxml->entry as $entry) {
        $media = $entry->children('http://search.yahoo.com/mrss/');
        $attrs = $media->group->player->attributes();
        $watch = $attrs['url']; 
        
        $attrs = $media->group->thumbnail[0]->attributes();
        $thumbnail = $attrs['url']; 
        preg_match_all('/\??v=([^&]+)&?/is',$watch,$url);
        
        $yt = $media->children('http://gdata.youtube.com/schemas/2007');
        $attrs = $yt->duration->attributes();
        $length = $attrs['seconds']; 
        
        $attrs = $media->group->category->attributes();
        $category = $attrs['label'];

        $attrs = $media->group->category->attributes();
        $termm = $media->group->category;

        
        $gd = $entry->children('http://schemas.google.com/g/2005'); 
        if ($gd->rating) {
          $attrs = $gd->rating->attributes();
          $rating = $attrs['average']; 
        } else {
          $rating = 0; 
        }
        $video_info[$video_count] = array($media->group->title,$entry->author->name,$watch,$category,$termm,$thumbnail,$length,$viewCount,$rating,$media->group->description,$url[1][1]);
        $video_count ++;
      }
      return $video_info;
}

function get_detail_video($v){
    $feedURL = 'http://gdata.youtube.com/feeds/api/videos/' . trim($v);
    $entry =  xml_fetch($feedURL);
    $title = $entry->title;
    $published = $entry->published;
    $updated = $entry->updated;
    $content = $entry->content;
    $name = $entry->author->name;

    $media = $entry->children('http://search.yahoo.com/mrss/');
    $attrs = $media->group->thumbnail[0]->attributes();
    $thumbnail = $attrs['url'];

    $yt = $media->children('http://gdata.youtube.com/schemas/2007');
    $attrs = $yt->duration->attributes();
    $length = $attrs['seconds']; 


    $gd = $entry->children('http://schemas.google.com/g/2005'); 
    if ($gd->rating) { 
        $attrs = $gd->rating->attributes();
        $rating = $attrs['average']; 
      } else {
        $rating = 0;         
    }

    $yt = $entry->children('http://gdata.youtube.com/schemas/2007');
    if ($yt->statistics){
        $attrs = $yt->statistics->attributes();
        $viewCount = $attrs['viewCount']; 
        $favorite = $attrs['favoriteCount'];
    } else{
        $viewCount = 0;
        $favorite = 0;
    }
    $result = array($v,$title,$published,$updated,$content,$name,$thumbnail,$rating,$favorite,$viewCount,$length);
    return $result;
}

function get_user_xml($v){
    $feedURL = 'http://gdata.youtube.com/feeds/api/users/' . trim($v);
    $entry =  xml_fetch($feedURL);
    $title = $entry->title;
    $published = $entry->published;
    $updated = $entry->updated;
    $author = $entry->author->name;
    
    $yt = $entry->children("http://gdata.youtube.com/schemas/2007");
    $age = $yt->age;
    $description = $yt->description;
    $sex = $yt->gender;
    $location = $yt->location;
    $occu = $yt->occupation;
    $arrs  = $yt->statistics->attributes();
    $subcount = $arrs['subscriberCount'];
    $viewcount = $arrs['viewCount'];
    $totalView = $arrs['totalUploadViews'];
    return array($title,$author,$published,$updated,$age,$sex,$description,$location,$occu,$subcount,$viewcount,$totalView);
}


function get_most_view(){
    $feedURL = make_url();
    return get_video_xml($feedURL);
}

function get_trends(){
    $feedURL = 'http://gdata.youtube.com/feeds/api/standardfeeds/on_the_web?&start-index=1&max-results=5';
    return get_video_xml($feedURL);
}

function get_favorite(){
    $feedURL = 'http://gdata.youtube.com/feeds/api/standardfeeds/top_favorites?time=today&start-index=1&max-results=5';
     return get_video_xml($feedURL);
}

function get_feature(){
     $feedURL = "http://gdata.youtube.com/feeds/api/standardfeeds/recently_featured?&start-index=1&max-results=5";
     return get_video_xml($feedURL);
}

function get_search($q,$start,$max){
     $q = str_replace(' ','+',$q);
     $feedURL = 'http://gdata.youtube.com/feeds/api/videos?q=' . $q . '&orderby=published&start-index=' . $start . '&max-results=' . $max;
     return get_video_xml($feedURL);
}

function get_related_video($v){
    $feedURL = 'http://gdata.youtube.com/feeds/api/videos/'. $v . '/related?v=2&start-index=1&max-results=10';
    return get_video_xml($feedURL);
}

function get_user_updates($user){
    $feedURL = 'http://gdata.youtube.com/feeds/api/users/'.$user.'/uploads';
    return get_video_xml($feedURL);
}


function get_user_info($v){
    $feedURL = 'http://gdata.youtube.com/feeds/api/users/' . $v;
    return get_user_xml($feedURL);
}

function get_uploads($user,$start,$max){
     $user = str_replace(' ','+',$user);
     $feedURL = 'http://gdata.youtube.com/feeds/api/users/' . $user . '/uploads/?start-index=' . $start . '&max-results=' . $max;
     return get_video_xml($feedURL);
}
?>
