<?php
include ("conn.php");

$table_1 = 'images';
$table_2 = 'xml';

$cre_ta = mysql_query("create table $table_1 (id int primary key auto_increment,url varchar(200) not null unique,content blob not null,fetch_time timestamp)",$db);
if (! $cre_ta)
  die( "create table $table_1 error <br/> ". mysql_error() ); 
else
  echo "create table $table_1 successful <br/>";

$cre_tb = mysql_query("create table $table_2 (id int primary key auto_increment,url varchar(200) not null unique,content mediumtext not null,fetch_time timestamp)",$db);
if (! $cre_ta )
  die( "create table $table_2 error <br/>". mysql_error() ); 
else
  echo "create table $table_2 successful <br/>";
?>