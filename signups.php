<?php 
$tripid = $_SESSION['tripid'];
$command = trim("python ./getsignups.py tripid");
$output = shell_exec($command);
$out = explode("\n", $output);


?>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="signups.css">
  <title>University Of Surrey Mountaineering</title>
</head>
<body>
    
    <header class = "Banner">
        <div><img src="Photos/edited-photo.png"></div>
        <div></div>
        <div class="login"><button onclick="location.href = 'login.php'">login</button></div>
    </header>

    <?php foreach ($out as $index => $counter): ?>
        <?php echo $counter ?>

    <?php endforeach; ?>

</body>
</html>
