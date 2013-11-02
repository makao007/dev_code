    <?php include ("./head.html"); ?>
    <div id="main">

        <?php include("common.php");
            $max = 10;
            $start = 1;
            if (isset($_GET['user'])){
                if(isset($_GET['start-index']))
                    $start = ((int)$_GET['start-index'] -1) * 10 +1;
                $video_info = get_uploads($_GET['user'],$start,$max);
            }
            else
                $video_info = get_most_view();

        ?>
            <div id="ltitle">
                Uploads : <?php echo $_GET['user']; ?>
            </div>

        <?php
            foreach ($video_info as $video){
        ?>
            <div id="lc_info_search">
                <div id="lc_info">
                    <a href="./detail.php?v=<?php echo $video[10]; ?>"><img src="<?php echo proxy_image($video[5]);?>"></a>
                    <span>
                    <p id="v_text"><?php echo $video[0]; ?></p>
                    <p id="v_desc"><?php echo $video[9]; ?></p>
                    Category: <b><a href="./most_view.php?term=<?php echo $video[4]; ?>"><?php echo $video[3]; ?></a></b>&nbsp;&nbsp;&nbsp;&nbsp;
                    By: <b><a href='./user.php?user=<?php echo $video[1]; ?>'><?php echo $video[1]; ?></a></b>&nbsp;&nbsp;&nbsp;&nbsp;
                    views: <b><?php echo $video[7]; ?></b>&nbsp;&nbsp;&nbsp;&nbsp;
                    Duration: <b><?php printf('%0.2f', $video[6]/60); ?></b>&nbsp;&nbsp;&nbsp;&nbsp;
                    Rating: <b><?php printf('%0.2f', $video[8]); ?> </b>
                    </span>
                </div>
            </div>
            <?php } ?>

    </div>
    
    <div id="bottom">

        <?php 
                if (isset($_GET['user']))
                    $n_url = '?user=' . $_GET['user'] . "&start-index=";
                else{
                    $n_url = '?start-index=';
                }
                if(isset($_GET['start-index']))
                    $page = (int) $_GET['start-index'];
                else
                    $page = 1;
                if ($page > 1){
                    echo "<a href='" . $n_url. strval($page-1). "'>Previous</a>  ";
                }
                if ($page < 10){
                    for($i=1; $i<10; $i++)
                        echo " <a href='". $n_url .$i."'> ".$i."</a>   ";
                }
                else{
                    $begin = floor($page/10);
                    for($i=0;$i<10;$i++)
                        echo " <a href='".$n_url.($i+$begin*10)."'> ".($i+$begin*10)."</a>   ";
                }
                echo "  <a href='".$n_url. strval($page+1)."'>Next</a>";
        ?>

        <br />
        <hr />
        &copy; 2011
    </div>
</body>
</html>
