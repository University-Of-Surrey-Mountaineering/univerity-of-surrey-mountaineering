<?php

session_start();

$forename = $surname = $committee = $email_address = $membernumber = $memberexp = $pfp = "";

if (!isset($_SESSION["ID"])){
    header("Location: login.php");
}
else {
    $ID = $_SESSION["ID"];
    $username = $_SESSION["Username"];
    $command = "python ./retrieveuserdetails.py " . $ID;
    $output = trim(shell_exec($command));
    $out = explode("\n", $output);
    $forename = $out[0];
    $surname = $out[1];
    $commitee = $out[2];
    $email_address = $out[3];
    $membercommand = "python ./retrievemembershipdetails.py " . $ID;
    $memberoutput = trim(shell_exec($membercommand));
    $memberout = explode("\n", $memberoutput);
    $membernumber = $memberout[0];
    $memberexp = $memberout[1];
    try {
        $pfp = $out[4];
    }

    catch (Exception $e) {
        $pfp = "Photos/000099290029.jpg";
    }

    if (!isset($_SESSION["Committee"]) and $commitee == 1) {
        $_SESSION["Committee"] = $commitee;
    }

    if (!isset($_SESSION["pfp"])) {
        $_SESSION["pfp"] = $pfp;
    }
}

$background_image = "Photos/IMG_0943.JPG";

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="dashboard.css">
  <title>University Of Surrey Mountaineering</title>
</head>
<body>
    
    <header class = "Banner">
        <div><img src="Photos/edited-photo.png"></div>
        <div></div>
        <div class="login"><button onclick="location.href = 'login.php'">login</button></div>
    </header>

    <div class="container">
        <div></div>
        <div id="container">
            <div class = "user_section">
                <div></div>
                <a class="member_details" href = "user.php">
                    <div class = "pfp_container" href="">
                        <div id = "pfp"></div>
                    </div>
                    <div class = "user_details">
                        <p> Username: 
                            <?php echo $username;?>
                        </p>
                        <p>Name: 
                            <?php echo $forename . " " . $surname;?>
                        </p>
                        <p>Email Address: 
                            <?php echo $email_address;?>
                        </p>
                        <p>Membership Code:
                            <?php echo $membernumber;?>
                        </p>
                        <?php if ($memberexp != "None"): ?>
                            <p>Expiry Date:
                                <?php echo $memberexp;?>
                            </p>
                        <?php endif;?>
                    </div>
                </a>
                <div></div>
                
                <style>
                    #pfp {
                        justify-content: center;
                        height:20vh;
                        width:10vw;
                        background-image: url(<?php echo $pfp;?>);
                        border-radius: 50%;
                        background-position: center;
                        background-size: auto 30vh;
                        background-repeat: no-repeat;
                    }
                </style>
            </div>
            <!--
            <div class="section">
                <div></div>
                <div class="next_trip">
                    
                    <a href = "trips.php">
                        gggg
                        <style>
                            .next_trip a {
                                margin: 5vh;
                                grid: flex;
                                justify-content: center;
                                justify-items: center;
                                background-color: white;
                                height: 20vh;
                                width: 20vw;
                                background:url(<?php echo $background_image;?>);
                                background-repeat: no-repeat;
                                background-size: 20vw auto;
                                border-radius: 20px;
                                background-position: center;
                            }
                        </style>
                    </a>

                </div>

                <div></div>
            </div>
                        -->
            <?php if (!($commitee != 1)): ?>
            <div class="section">
                <div></div>
                <div>
                    <a href = "approvemember.php">Approve members</a>
                </div>
                <div></div>
            </div>
            <?php endif;?>
        </div>
        <div></div>
    </div>

</body>
</html>