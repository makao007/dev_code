<?php
include ("./head.html");
if (isset($_GET['v']))
    $v = $_GET['v'];
else
    $v = 'v';
?>

    <div id="main">
        <div id="left">
            <?php include ("common.php"); $result = get_detail_video($v); ?>
            <div id="ltitle"><?php echo $result[1]; ?></div>
            <embed src="player.swf" quality="high" allowfullscreen="true" 
            wmode="Transparent" type="application/x-shockwave-flash" width=620 height=380 
            flashvars="file=./fetch_video.php?v=<?php echo $v ?>.flv&autostart=true&image=<?php echo proxy_image($result[6]); ?>">
            </embed>
                <div id="sub-description">Presented by <a href="./user.php?user=<?php echo $result[5]; ?>"><?php echo $result[5]; ?></a>
                Published: <?php echo substr(str_replace("T",'  ',$result[2]),0,-5); ?>
                &nbsp;&nbsp;Updated: <?php echo substr(str_replace("T",'  ',$result[3]),0,-5); ?><br/>
                Rating: <b><?php echo $result[7]; ?></b>&nbsp;&nbsp;
                Favorite: <b><?php echo $result[8]; ?></b>&nbsp;&nbsp;
                Duration: <b><?php printf("%.2f",$result[10]/60); ?></b>min&nbsp;&nbsp;
                ViewCount: <b><?php echo $result[9]; ?></b> <br/><br/>
                <?php echo $result[4]; ?>
                </div>

            </div>
        </div>
        <div id="right">
            <div id="rtitle">Related Videos</div>
            <?php
                $video_info_f = get_related_video($v);
                foreach($video_info_f as $video){
            ?>
            <div id="sub-project">
                <div id="sub-info">
                    <div id="sub-info-detail">
                    <a href="./detail.php?v=<?php echo $video[10]; ?>"><img src="<?php echo proxy_image($video[5]);?>" /></a>
                        <span><p><?php echo $video[0]; ?></p>
                        by <a href='./user.php?user=<?php echo $video[1]; ?>'><?php echo $video[1]; ?></a><br/>
                        <?php echo $video[7]; ?>views, 
                        <?php printf("%.2f",$video[6]/60); ?>min
                        </span>
                    </div>
                </div>
            </div>
            <?php }  ?>

        </div>
    </div>

<?php include ("./tail.html"); ?> 
