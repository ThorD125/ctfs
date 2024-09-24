this box showed a http and ssh server

on the website there is a login
on /login/login.php
going to the directory lists multiple files

and it has a file login.php.swp
this file can be reversed with vim -r login.php.swp

strcmp
compares 2 things and bcs it uses == to check if its 0
but not === 
we can change the username string to an array from changing it in a the request
from username => username[]
same with the password
and login without a valid password

then uploading a shell and get a reverseshell

cat ./config.php
we find admin:thisisagoodpassword


and in the /home dir we find a user john

trying the password with john to login with ssh we get in
sudo -l we can run find as root
sudo /usr/bin/find /root/root.txt -exec cat {} \;