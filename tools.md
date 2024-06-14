# Tools

ping {IP}
nmap

subfinder
httpx
whatweb
gobuster
dirb

ftp anonymous@{IP}

smbclient -L={IP} #list shares on target with anomouse
smbclient -L={IP} -U Administrator #try a login
smbclient //{IP}/{sharename} #connect to specifiec share
RECURSE ON
PROMPT OFF
cd {dir}
mget *

hydra -L users.txt -P pass.txt {IP} ssh

whoami
id #default groups: audio video plugdev cdrom dip floppy netdev
groups

pspy32 #spy tool, open it on a host, relogin on second terminal

ss -tln #identify localports
ss -tla #identify name

ssh -L {porttoconnectwithonlocalhost}:{local/iptoconnecttothroughthessh}:{porttoconnect} {USER}@{IP}

psql -U {USER} -h {IP} -p 5432
\l #list databases
\c {name} #connect to a database
\dt #list tables
select * from {table} #show table content


zip@john file.zip>hashes.lst
john hashes.lst
john hashes.lst --show

hashcat

xfreerdp /v:{IP} /u:{USER} /p:{PASSWORD}

flask-unsign
metasploit
nc

ilspy

dirbuster
gobuster
feroxbuster