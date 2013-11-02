<?php
    $db_host = 'localhost';
    $db_user = 'yaya1234_test';
    $db_pawd = 'heliohost1234';
    $db_schema = "yaya1234_yt";

    $db_table_image = "images";
    $db_table_xml = "xml";
    $db = mysql_connect($db_host,$db_user,$db_pawd);
    if(!$db)
        die(mysql_error());
    mysql_select_db($db_schema,$db);

?>
