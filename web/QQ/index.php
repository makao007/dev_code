<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>在线聊天 -- mkw-chat</title>
    <link rel="stylesheet" href="./css/pub.css" type="text/css" media="screen" charset="utf-8">
    <link rel="stylesheet" href="./css/main.css" type="text/css" media="screen" charset="utf-8">
    <link rel="stylesheet" href="./css/main_2.css" type="text/css" media="screen" charset="utf-8">

</head>
<body>

<?php
    include ('./html/main_panel.html');      // 显示好友，群，自己信息的主要界面
    include ('./html/stat.html');            // 页面底部的状态
    include ('./html/friend_chat.html');     // 好友之间的聊天窗口
    include ('./html/zone_chat.html');       // 群聊天
    include ('./html/login.html');           // 登录窗口
    include ('./html/register.html');        // 用户注册窗口
    include ('./html/forgot_password.html'); // 忘记密码
?>

<script type="text/javascript" charset="utf-8" src="./js/main_1.js"></script> 
<script type="text/javascript" charset="utf-8" src="./js/main_2.js"></script> 
<script type="text/javascript" charset="utf-8" src="./js/init.js"></script> 
<script type="text/javascript" charset="utf-8" src="./js/func.js"></script> 

</body>
</html>
