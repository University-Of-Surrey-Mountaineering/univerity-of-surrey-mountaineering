<?php 
session_start();
$command = trim("python ./getallcommittee.py");
$output = shell_exec($command);
$out = explode("\n", $output);

function testdata($string) {
  if ($string[0] == "("){
    return substr($string, 2, -1);
  }
  elseif (substr($string, -1) == ")"){
    return substr($string, 2, -2);
  }
  else {
    return substr($string, 2, -1);
  }
}

function fixcommittee($string) {
  $arr = explode(",", $string);
  $commitarr = [];
  foreach ($arr as $c => $i){
    $commitarr[] = testdata($i); 
  }
  return $commitarr;
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="index.css">
  <title>University Of Surrey Mountaineering</title>
</head>
<body>
  <header class = "Banner">
    <div><img src="Photos/edited-photo.png"></div>
    <div>
      <a href="dashboard.php" class = "dashboardlink">Dashboard</a>
    </div>
    <style>
      .dashboardlink {
        border-radius: 5%;
        background-color: #3c3c3c;
        padding-left: 1%;
        padding-right: 1%;
        padding-top: 1%;
        padding-bottom: 1%;
      }
    </style>
    <?php if (!isset($_SESSION["ID"])): ?>
      <div class="login"><button onclick="location.href = 'login.php'">login</button></div>
    <?php else: ?>
      <div id = "container">
        <a href="user.php">
          <?php

          $ID = $_SESSION["ID"];
          $Username = $_SESSION["Username"];
          $usercommand = trim("python ./retrieveuserdetails.py " . $ID);
          $useroutput = shell_exec($usercommand);
          $userout = explode("\n", $useroutput);
          
          try {
              $userpfp = $userout[4];
          }
          catch (Exception $e) {
              $userpfp = "Photos/000099290029.jpg";
          }
          ?>
        <div class = "pfp_container">
          <div id = "userpfp"></div>
          <p id = "username"><?php echo $Username;?></p>
        </div>
        </a>
        <style>
          #userpfp {
            background-image: url(<?php echo $userpfp;?>);
            height: 10vh;
            width: 5vw;
            background-size:auto 10vh;
            background-repeat: no-repeat;
            background-position: center;
            border-radius: 50%;
          }
          #container {
            width: 20vw;
          }

          .pfp_container {
            height: 13vh;
            width:fit-content;
            padding-left: 5%;
            padding-right: 5%;
            border-radius: 10%;
            border-style: solid;
            margin-top: 1%;
            background-color: #3c3c3c;
          }
          #username {
            margin-left: 5%;
            margin-right: 5%;
          }
        </style>
      </div>
    <?php endif; ?>
  </header>   

  <div class = "Header">
    <div></div>
    <div class="Header_Container">
      <div class="Logo"><img src="Photos/edited-photo.png"></div>
    </div>
    <div></div>
  </div>

  <div class="description">
    <div>
      <h2>We are a friendly and welcoming club with a shared passion for climbing and mountaineering. Whether you're a complete beginner or an experienced climber, we offer something for everyone! Our weekly climbing sessions take place at Surrey Summit, where you can develop your skills, meet like-minded people, and have fun. We also organize regular trips, including outdoor climbing, mountain climbing and hiking, and unparalleled vibes. community is at the heart of what we do, ensuring a supportive and friendly environment for all. Join us for exciting challenges, breath-taking views, and an amazing community full of energy and good vibes!</h2>
      <h3>
Weekly activities:<br>
Monday climbing session - 7pm to 9pm<br>
Wednesday climbing session - 3pm to 5pm<br>
Friday climbing session - 7pm to 9pm</h3>
<h4>

What we also do: <br>
- Regular socials! (both drinking and non-drinking) <br>
- Amazing trips... such as our annual trips to Ailefroide in the French Alps.<br>
- Top rope and lead climbing training all included in your membership <br>
  </h4>
</div>
</div>

  <div class = "commitcont">
    <?php foreach ($out as $index => $counter): ?>
      <?php if ($counter != ""): ?>
        <?php
          $member = fixcommittee($counter);
          $fullname = $member[0] . " " . $member[1]; 
          $pfp = $member[2];
          $rolename = $member[3];
          $about = $member[4];
        ?>
        <div></div>
        <div class="committee">
            <div class = "pfp">
              <div id="pfp<?php echo $index;?>"></div>
            </div>
            <div class = "desc">
              <div class="about">
                <div>
                  <p>My name is: <?php echo $fullname;?></p>
                  <p>Role: <?php echo $rolename;?></p>
                </div> 
              </div>
              <div class = "about">
                <div>
                  <b>About me:</b>
                  <p class = "text"><?php echo $about;?> </p>
                </div>  
              </div>
            </div>
            <br>

            <style>
              #pfp<?php echo $index; ?> {
                display: flex;
                align-items: center;
                justify-items: center;
                justify-content: center;
                height:50vh;
                width:25vw;
                background-image: url(<?php echo $pfp;?>);
                border-radius: 50%;
                background-position: center;
                background-size: auto 100%;
                background-repeat: no-repeat;
                margin: 1%;
                }
            </style>
        </div>
        <div></div>
        <?php endif; ?>
    <?php endforeach; ?>
  </div>


</body>
</html>