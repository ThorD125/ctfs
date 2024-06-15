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

ssh {user}@{ip}
whoami
id #default groups: audio video plugdev cdrom dip floppy netdev
groups
cat .bash_history

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

hashcat -a 0 -m 20 hashfile /usr/share/wordlists/rockyou.txt

xfreerdp /v:{IP} /u:{USER} /p:{PASSWORD}

flask-unsign
metasploit
nc

ilspy

dirbuster

gobuster dir --url {ip} --wordlist /usr/share/wordlists/dirb/big.txt
gobuster dns -d {domain} --wordlist /usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt

feroxbuster -u {ip}

ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -u http://{domain} -H 'Host: FUZZ.{domain}' -fw 4 -t 100
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt:FFUZ -u http://dev.devvortex.htb -H 'Host: http://dev.devvortex.htb/FFUZ' -ic -t 100
