<?php
include ("./head.html");
if (isset($_GET['user']))
    $v = $_GET['user'];
else
    return;
?>

    <div id="main">
        <div id="left">
<?php 
    include ("common.php"); 
    $video_info_f = get_user_updates($v);
    $result = $video_info_f[0];
?>
            <div id="ltitle"><?php echo $result[0]; ?></div>
            <div id="player" style="width:620; height:380">
                <embed src="player.swf" quality="high" allowfullscreen="true" 
                wmode="Transparent" type="application/x-shockwave-flash" width=620 height=380 
                flashvars="file=./fetch_video.php?v=<?php echo $result[10]; ?>.flv&image=./aa.jpg;">
                </embed>
            </div>
                <div id="sub-description"> <br />
                Published: <?php echo substr(str_replace("T",'  ',$result[11]),0,-5); ?>
                &nbsp;&nbsp;Updated: <?php echo substr(str_replace("T",'  ',$result[12]),0,-5); ?><br/>
                Rating: <b><?php echo $result[8]; ?></b>&nbsp;&nbsp;
                Duration: <b><?php printf("%.2f",$result[6]/60); ?></b>min&nbsp;&nbsp;
                ViewCount: <b><?php echo $result[7]; ?></b> 
                <hr />
                <h4>Profile</h4>
                <?php $result=get_user_xml($v);  ?>
                <?php echo $result[0]; ?> <br/>
                Published: <?php echo substr(str_replace("T",'  ',$result[2]),0,-6); ?>&nbsp;&nbsp;
                Updated: <?php echo substr(str_replace("T",'  ',$result[3]),0,-6); ?><br/>
                <?php if(strtolower($result[5])=='m') echo 'Male'; else echo 'Female'; ?><br/>
                Age : <?php echo $result[4]; ?> </br>
                Location: <?php echo $result[7]; ?> <br/>
                <?php echo $result[6]; ?>
                </div>
        </div>
        <div id="right">
            <div id="rtitle"><a href="./uploads.php?user=<?php echo $v; ?>">Uploads</a></div>
            <div style="height:500px; overflow:scroll;">
            <?php
                foreach($video_info_f as $video){
            ?>
            <div id="sub-project" >
                <div id="sub-info" >
                    <div id="sub-info-detail">
                    <a href="/detail.php?v=<?php echo $video[10]; ?>" onclick="xx('<?php echo $video[10]; ?>'); return false;" ><img src="<?php echo proxy_image($video[5]);?>" /></a>
                        <span><p><?php echo $video[0]; ?></p>
                        <?php echo $video[7]; ?>views, 
                        <?php printf("%.2f",$video[6]/60); ?>min
                        </span>
                    </div>
                </div>
            </div>
            <?php }  ?>
            </div>

        </div>
    </div>
    
    <div id="bottom">
        <br />
        <hr />
        &copy; 2011
    </div>
    </body>
    <script type="text/javascript" charset="utf-8">
        function xx(id){
            var dd = document.getElementById('player');
    dd.innerHTML = '<embed src="player.swf" quality="high" allowfullscreen="true" wmode="Transparent" type="application/x-shockwave-flash" width=620 height=380 flashvars="file=./fetch_video.php?v=' + id +'.flv&autostart=true">';
        }
    </script>

</html>
