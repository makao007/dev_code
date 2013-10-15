<?php
include ("conn.php");

//联系人
//状态stat: n离线; y在线; h隐身; l离开
$user = "create table if not exists user (
    uid int primary key auto_increment,
    name varchar(100) not null unique,
    pawd char(32) not null,
    nickname char(100),
    signed varchar(500),
    state char(1) ) engine=innodb";

//联系人详细信息
$person_info = "create table if not exists person_info (
    pid int primary key auto_increment,
    uid int ,
    sex char(1) not null,
    created datetime,
    description varchar(500),
    foreign key (uid) references user(uid) on delete cascade ) engine=innodb";

//群
$zone = "create table if not exists zone (
    zid int primary key auto_increment,
    name varchar(100),
    description varchar(500),
    msg varchar(500),
    created datetime,
    owner int )";

//群成员
//角色proid : o创建者，m管理员， s普通成员
$zone_member = "create table if not exists zone_member (
    zid int ,
    uid int ,
    name varchar(100),
    last_speak datetime,
    join_time datetime,
    proid char(1),
    primary key (zid,uid) )";

//好友列表
$friends = "create table if not exists friends (
    owner int ,
    friend int,
    category int,
    created datetime,
    primary key (owner,friend),
    foreign key (owner)  references user(uid) on delete cascade,
    foreign key (friend) references user(uid) on delete cascade ) engine=innodb";

//好友分类
$friend_category = "create table if not exists friend_category (
    cid int,
    name varchar(50),
    owner int,
    primary key (cid,owner),
    foreign key (owner) references user(uid) on delete cascade ) engine=innodb";

//用户与群
$user_zone = "create table if not exists user_zone (
    uid int,
    zid int,
    primary key (uid,zid))";

// 消息, type: s:系统(只读)，u:用户(聊天), z:群(聊天), f:是否添加好友, m:是否允许进群    readed:默认未读
$message = "create table if not exists message (
    mid int primary key auto_increment,
    type char(1),
    mfrom int not null,
    mto int,
    readed char(1) default 'n',
    content varchar(1024),
    created datetime )";
    

function create_table ($sql,$table){
    global $db;
    $result = mysql_query($sql,$db);
    if (! $result)
        die("创建表 $table 失败<br>" . mysql_error());
    else
        echo "成功创建表 $table<br>";
} 

mysql_query ("set names utf8");

create_table ($user,"联系人");
create_table ($person_info, "联系人详细信息");
create_table ($zone, "群");
create_table ($zone_member,"群成员");
create_table ($friends,"好友");
create_table ($friend_category,"好友分类");
create_table ($user_zone,"用户所加入的群");
create_table ($message, "消息");

?>
