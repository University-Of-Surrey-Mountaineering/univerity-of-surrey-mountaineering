<?php 

session_start();
$tripid = $_SESSION['tripid'];
$tripname = $_SESSION['tripname'];
$userid = $_SESSION['ID'];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $pronouns = $_POST['pronouns'];
    $phonenum = $_POST['phonenum'];
    $harness = $_POST['harness'];
    $helmet = $_POST['helmet'];
    if ($harness != "on") {
        $harness = "none";
    }
    if ($helmet != "on") {
        $helmet = "none";
    }
    $bmcmember = $_POST['bmcmember'];
    $emergencycont = $_POST['emergencycont'];
    $relation = $_POST['relation'];
    $emgnumber = $_POST['emgnum'];
    $medconditions = $_POST['medconditions'];
    $command = trim("python ./signup.py " . $tripid . " " . $userid . " " . $pronouns . " " . $phonenum . " " . $harness . " " . $helmet . " " . $bmcmember . " " . $emergencycont . " " . $relation . " " . $emgnumber . " " . $medconditions);
    echo $command;
    $output = shell_exec($command);
    $out = explode("\n", $output);
}



?>



<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="signup.css">
        <title>University Of Surrey Mountaineering</title>
        </head>
    <body>
        <header class = "Banner">
            <div><img src="Photos/edited-photo.png"></div>
            <div></div>
            <div class="login"><button onclick="location.href = 'login.php'">login</button></div>
        </header>

    <div>
        <h1><?php echo $tripname; ?></h1>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
            <h3>Climbing, hill walking and mountaineering are activities with a danger of personal injury or death.
                 Participants in these activities should be aware of and accept these risks and be responsible
                  for their own actions and involvement. The club where possible will provide equipment and training to reduce the risks of such activities.
                   Correct use of this knowledge and equipment remains the responsibility of the individual.</h3>
            <label for="termsandconditions">I understand and agree to the above statement: </label>
            <input type="radio" name = "termsconditions" value="yes" required>
            <br>
            <label for="pronouns">Preferred pronouns: </label>
            <input type = "text" name="pronouns">
            <br>
            <label for="phonenum"> Your phone number <br> Please include country code (+44 for UK) <br></label>
            <input type= "tel" name = "phonenum" required>
            <br>
            <label for="harness">Do you need any kit?</label>
            <br>
            <label for="hanress">harness:</label>
            <input type = "checkbox" name= "harness">
            <label for="helmet">helmet:</label>
            <input type = "checkbox" name = "helmet">
            <br>
            <label for="bmcmember">Do you have bmcmembership (If you are unsure reply no)</label>
            <br>
            <label for="bmcmember">Yes:</label>
            <input type = "radio" name="bmcmember" value="yes">
            <label for="bmcmember">No:</label>
            <input type="radio" name = "bmcmember" value="no">
            <br>
            <label for="emergencycont">Please enter the name of your emergency contact:</label>
            <input type="text" name = "emergencycont" required>
            <br>
            <label for="relation">What is their relation to you:</label>
            <input type="text" name="relation" required>
            <br>
            <label for="emgnum">Please enter their phone number:</label>
            <input type="tel" name="emgnum" required>
            <br>
            <label for="medconditions">Are there any medical conditions we should know about?</label>
            <textarea type="text" name="medconditions"> </textarea>
            <br>
            <input type="submit" name="formsubmit" value="Submit">
        </form>
    </div>
    </body>
</html>
