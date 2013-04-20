<?php
function is_user(){
    @session_start();
    if (isset($_SESSION['id']))
        return 1;
    else
        to_login();
}


function is_login(){
    @session_start();
    if (isset($_SESSION['id']))
        return 1;
    else
        return 0;
}

function to_login(){
    Header("Location: /");
    exit;
}

function get_user (){
    @session_start();
    return ($_SESSION['id']);
}

function get_username (){
    @session_start();
    return ($_SESSION['username']);
}

function has_unsafe_char($str){
    $chars = array(" ","/","\\",'"',"'","=",">",'<');
    foreach ($chars as $value)
        if (strpos($str,$value))
            return 1;
    return 0;
}

function get_header($key){
    if (isset($_GET[$key]))
        return urldecode(remove_unsafe_char($_GET[$key]));
    else
        return '';
}

function remove_unsafe_char($str){
    $temp = $str;
    $chars = array(" ","/","\\",'"',"'","=",">",'<');
    foreach ($chars as $value)
        $temp = str_replace($value,'',$temp);
    return $temp;
}

function referer ($str){
    if (! isset ($_SERVER['HTTP_REFERER']))
        $url = $str;
    else
        $url = $_SERVER['HTTP_REFERER'];
    return $url;
}

function utf8(){
    header("Content-type: text/html; charset=utf-8");
}

function err_msg ($str){
    return "{status:0, info:[], text:'$str'}";
}

function suc_msg ($msg,$info=array()) {
    return "{status:1, text:'$msg', info: $info}";
}

?>
