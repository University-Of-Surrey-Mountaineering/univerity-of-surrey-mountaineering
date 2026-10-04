<?php

if (isset($_SESSION["ID"])) {
  unset($_SESSION["ID"]);
  unset($_SESSION["Username"]);
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

function save_data($output) {
  $out = explode("\n", $output);
  if (count($out) == 2) {
    
    $ID = $out[0];
    $uname = $out[1];
    if(isset($_SESSION["ID"])) {
      unset($_SESSION["ID"]);
      unset($_SESSION["uname"]);
    }
    $_SESSION["ID"] = $ID;
    $_SESSION["Username"] = $uname;
    header("Location: dashboard.php");
  }

  else {
    throw new Exception($output);
  }

  
}

session_start();
$output = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $uname = test_input($_POST["UserName"]);
  $pword = test_input($_POST["Password"]);
  $command = "python ./login.py " . $uname . " ".  $pword;
  $output = trim(shell_exec($command));
  try{
    save_data($output);
    $output = "";
  }
  catch (Exception $e) {}

}

$testout = $output;
?>



<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="login.css">
  <title>University Of Surrey Mountaineering</title>
</head>
<body>
  <div class = "login">
    <div></div>
    <div class="container">
      <div class = section>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
          <div>
            <label for="Uname">Username: </label>
            <input type="text" id="Uname" name = "UserName">
          </div>
          <div>
            <label for="Pword">Password: </label>
            <input type="text" id="Pword" name = "Password">
          </div>
          <div>
            <input type="submit" value="Login">
            <?php echo $testout; ?>
          </div>
        </form>
        <button onclick="location.href = 'createprofile.php'">create a profile</button>
        </div>
      </div>
      <div></div>
  </div>
  
</body>
</html>