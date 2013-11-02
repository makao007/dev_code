    <?php include("./head.html"); ?>
    <div id="main">
            <div id="ltitle"><a href="./most_view.php">Most Popular</a></div>

<?php  
include("common.php");
$video_info = get_most_view();
foreach($video_info as $video){
?>
            <div id="lcategory">
                <div id="lctitle"><a href="?term=<?php echo $video[4]; ?>"><?php echo $video[3]; ?></a></div>
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
<?php }  ?>


        </div>
    </div>

    <div id="bottom">
        <br/>
        <?php 
                if (isset($_GET['term']))
                    $n_url = '?term=' . $_GET['term'] . "&start-index=";
                else
                    $n_url = '?start-index=';
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
        <br/>
        <hr/>
        &copy; 2011
    </div>
</body>
</html>

