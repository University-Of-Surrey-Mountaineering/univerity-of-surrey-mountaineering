<?php

session_start();
$approvalid = "";
$ID = $_SESSION["ID"];
$out = "";
$requestphoto = "";
if (!isset($_SESSION["ID"])){
    header("Location: login.php");
}
else {
    try {
        $command = "python ./getapproverequests.py";
        $output = trim(shell_exec($command));
        $out = explode("\n", $output);
        $approvalid = $out[0];
        $memberid = $out[1];
        $requestphoto = $out[3];
    }
    catch (Exception $e) {}


}
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    if ($_POST['accept'] == 'accept') {
        $command = "python ./updaterequest.py " . $approvalid . " " . $ID . " " . $memberid . " " . $_POST['type'] . " " . "1";
        $output = trim(shell_exec($command));
        $out = explode("\n", $output);
        $out = $out[1];
        header("Location: approvememberprocess.php");
    }
    elseif ($_POST['deny'] == 'deny') {
        $command = "python ./updaterequest.py " . $approvalid . " " . $ID . " " . $memberid . " " . $_POST['type'] . " " . "-1";
        $output = trim(shell_exec($command));
        $out = explode("\n", $output);
        $out = $out[1];
        header("Location: approvememberprocess.php");
    }
}

?>



<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="approvemember.css">
  <title>University Of Surrey Mountaineering</title>
</head>
<body>
    
    <header class = "Banner">
        <div><img src="Photos/edited-photo.png"></div>
        <div></div>
        <div class="login"><button onclick="location.href = 'login.php'">login</button></div>
    </header>
    <div id="section">
        <div></div>
        <div class = "section">
            <div>
                <?php if ($approvalid != "There are no approval requests"): ?>
                    <div class="photo">
                        <div></div>
                        <div class="container">
                            <img id = "photo" src="<?php echo $requestphoto; ?>">
                        </div>
                        <div></div>
                    </div>
                    <br>
                    <div class="submit">
                        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?> " method = "post">
                            
                            <input type="radio" name = "type" value = "semester" required> semester
                            <input type="radio" name = "type" value="year" required> year
                            <br>
                            <input type = "submit" name = "accept" value="accept"/>
                            <input type= "submit" name = "deny" value="deny" />
                        </form>
                        <? echo $out; ?>
                    </div>
                <?php else:?>
                    <div>
                        <h1>There are no current approval requests</h1>
                    </div>
                
                <?php endif; ?>
            </div>
        </div>
        <div></div>
    </div>
</body>
</html>