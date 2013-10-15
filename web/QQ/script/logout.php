<?php

@session_start();
unset($_SESSION['username']);
unset($_SESSION['id']);
echo (suc_msg('注销成功'));
?>

