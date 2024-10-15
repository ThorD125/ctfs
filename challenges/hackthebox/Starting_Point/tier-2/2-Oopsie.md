this box runs an ssh and a web service

on the website there is a js file
in the url:
'/cdn-cgi/login/'

thus going there is a login,
with a guest login

after login in
there are multiple parts of a site

and the account url has a parameter for what user we are,
changing this 2 to 1
shows the id of the admin user and email

using the role:admin, id:idoftheadmin

we could try to view the uploads page wich was earlier unreachable,

now uploading a reverse shell
and accesing it,
checking the environment
we find in the '/cdn-cgi/login/', there is one nice file, db.php
it conains the password and a table for the user robert

logging in through ssh succeeds witht his password

after login in
we can see the user robert has a group called "bugtracker"

`find / -group bugtracker 2>/dev/null`
looking for anything that group has access to we found an executable
this gets an input for the fileename
and cat it with a the filename

`file {found_file}` shows us the file includes an suuid (Set owner User ID)
this makes it so the file does not execute with the user permissions
but with the permisions of the person who set the permissions

and as its using cat and not the full path
we can abuse it
to privilege escalate

by changing the path

add a file called cat
change path,
`echo /bin/sh > /tmp/cat
chmod +x /tmp/cat
export PATH=/tmp:$PATH
{found_file}`
