<?php

function list_files($dir) {
    if(is_dir($dir)) {
        $files = scandir($dir);
        sort($files);
        foreach($files as $file) {
            if($file != "." && $file != "..") {
                if(is_dir($dir.'/'.$file)) {
                    list_files($dir.'/'.$file);
                } else {
                    echo '<a href="' . $dir.'/'.$file . '">' . $dir.'/'.$file . '</a><br>';
                }
            }
        }
    }
}

list_files('.');

?>