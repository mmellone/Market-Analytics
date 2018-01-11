<html>
<head>
  Stock Information
</head>
<body>
  <?php
    $symbol = htmlspecialchars($_GET['symbol_search']);
  ?>
  <br><br>
  Fetching data from stock symbol <?php echo $symbol; ?>.
  <br><br>
  <?php
    $mysqli = new mysqli("localhost", "root", "14jd3kpb", "stockdata");
    if ($mysqli->connect_errno) {
      echo "Failed to connect to MySQL: " . $mysqli->connect_error . "\n";
    } else {
      echo "Connected to MySQL server", PHP_EOL;
    }

    echo "Querying\n\n";
    $res = $mysqli->query("SELECT * FROM compiled_data WHERE Stock_Symbol= " . $symbol);
    var_dump($res);
    // $row = $res->fetch_assoc();
    // echo $row['_msg'];
  ?>
</body>
</html>
