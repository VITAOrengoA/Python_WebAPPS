<?php
    $servername = "dpg-co6tf4fsc6pc738bpj70-a.oregon-postgres.render.com"; // or your database server name
    $username = "dbvita_user"; // your database username
    $password = "a1nTA6Rw06fZrFwEFw9J29MkaYwrIEcn"; // your database password
    $dbname = "dbvita"; // your database name

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
?>
 