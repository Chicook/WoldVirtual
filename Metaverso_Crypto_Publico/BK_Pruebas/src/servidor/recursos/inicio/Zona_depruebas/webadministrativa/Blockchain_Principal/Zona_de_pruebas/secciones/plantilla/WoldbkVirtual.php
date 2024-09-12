// web principal.

<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $message = $_POST["message"];

    if (!empty($message)) {
        $filePath = "messages.txt";

        // Open the file for appending
        $file = fopen($filePath, "a");

        if ($file) {
            // Append the message to the file
            fwrite($file, $message . PHP_EOL);

            // Close the file
            fclose($file);
        }
    }
}
?>
