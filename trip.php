<?php
session_start();
$tripid = $_POST["tripid"];
$command = trim("python ./getalltrips.py " . $tripid);
$output = shell_exec($command);
$out = explode("\n", $output);
$tripname = $out[0];
$tripdate = $out[1];
$details = $out[2];
$_SESSION["tripid"] = $tripid;
$_SESSION["tripname"] = $tripname;
?>

<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="trip.css">
    <title>University Of Surrey Mountaineering</title>
    </head>
    <body>
        
        <header class = "Banner">
            <div><img src="Photos/edited-photo.png"></div>
            <div></div>
            <div class="login"><button onclick="location.href = 'login.php'">login</button></div>
        </header>


        <div>
            <div>
                <h1><?php echo $tripname; ?></h1>
                <h2><?php echo $tripdate ?></h2>
                <h3><?php echo $details ?></h3>
                <a href = "signup.php">
                    Sign up
                </a>
                <br>
                <?php if ($_SESSION['Committee'] == 1): ?>
                    <a href="signups.php">Signups</a>
                <?php endif; ?>

            </div>

        </div>

    </body>
</html>