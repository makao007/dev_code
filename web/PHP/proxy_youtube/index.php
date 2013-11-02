    <?php include ("./head.html"); ?>
    <div id="main">
        <div id="left">
             <a href="./most_view.php"><div id="ltitle">Most Popular</div></a>

    <?php include("common.php");
    $video_info = get_most_view();
    $video_info_f = get_feature();
    $video_info_fa = get_favorite();
    $video_info_t = get_trends();
    foreach ($video_info as $video){
?>
            <div id="lcategory">
                <div id="lctitle"><a href="./most_view.php?term=<?php echo $video[4]; ?>"><?php echo $video[3]; ?></a>
                </div>
                <div id="lc_info">
                    <a href="./detail.php?v=<?php echo $video[10]; ?>"><img src="<?php echo proxy_image($video[5]);?>"></a>
                    <span><p id="v_title"><?php echo $video[0]; ?></p>
                    By: <a href='./user.php?user=<?php echo $video[1]; ?>'><?php echo $video[1]; ?></a><br/>
                    views: <?php echo $video[7]; ?><br/>
                    Duration: <?php printf('%0.2f', $video[6]/60); ?><br/>
                    Rating: <?php printf('%0.2f', $video[8]); ?> 
                    </span>
                </div>
            </div>
        <?php } ?>

        </div>
        <div id="right">

            <div id="rtitle">Favorite</div>
            <?php foreach($video_info_fa as $video){ ?>
            <div id="sub-info">
                <div id="sub-info-detail">
                    <a href="./detail.php?v=<?php echo $video[10]; ?>"><img src="<?php echo proxy_image($video[5]);?>" /></a>
                    <span><p><?php echo $video[0]; ?></p>
                    by <a href='./user.php?user=<?php echo $video[1]; ?>'><?php echo $video[1]; ?></a><br/>
                    <?php echo $video[7]; ?>views, 
                    <?php printf('%0.2f', $video[6]/60); ?>min
                    </span>
                </div>
            </div>
            <?php }  ?>


            <div id="rtitle">Trends</div>
            <?php foreach($video_info_t as $video){ ?>
            <div id="sub-project">
                <div id="sub-info">
                    <div id="sub-info-detail">
                    <a href="./detail.php?v=<?php echo $video[10]; ?>"><img src="<?php echo proxy_image($video[5]);?>" /></a>
                        <span><p><?php echo $video[0]; ?></p>
                        by <a href='./user.php?user=<?php echo $video[1]; ?>'><?php echo $video[1]; ?></a><br/>
                        <?php echo $video[7]; ?>views, 
                        <?php printf('%0.2f', $video[6]/60); ?>min
                        </span>
                    </div>
                </div>
            </div>
            <?php }  ?>

            <div id="rtitle">Featured</div>
            <?php foreach($video_info_f as $video){ ?>
            <div id="sub-project">
                <div id="sub-info">
                    <div id="sub-info-detail">
                    <a href="./detail.php?v=<?php echo $video[10]; ?>"><img src="<?php echo proxy_image($video[5]);?>" /></a>
                        <span><p><?php echo $video[0]; ?></p>
                        by <a href='./user.php?user=<?php echo $video[1]; ?>'><?php echo $video[1]; ?></a><br/>
                        <?php echo $video[7]; ?>views, 
                        <?php printf('%0.2f', $video[6]/60); ?>min
                        </span>
                    </div>
                </div>
            </div>
            <?php }  ?>


        </div>
    </div>

<?php include("./tail.html"); ?>
