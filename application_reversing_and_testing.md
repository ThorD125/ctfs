# this:
is a bit of a guide into reversing and exploiting apps
work an a dedicated vm, turn of any usb or any outgoing connection
turn of wifi
and always create a clean snapshot before doing anything

## before doing anything
get the filehash
and make a copy, and use the copy to work with

## static analysis
### what the binary/file
magicbytes are the first x bytes that can help you determine what kynd of file it is fe a picture an executable etc
a hexeditor can be used to edit these or even any byte of a file

### strings 
of files checks valid text strings in files
sometimes revealing secrets

### packed files
sometimes files are obfuscated or are packed (like zips)
and can be deobfuscated or unpacked
exeinfo or peid can be used to detect this

### windows exes
peheaders contain a lot of info, "pe studio" allows you to look at these
"dependency walker" can help you identify what functionality an exe has


### decompiling
ilspy: .net

## dynamic analysis
### sandboxes
sandboxie can be used to sandbox an app
use process explorer to check the processes
fake or spoof the network: apatedns, fakedns.py, inetsim, fakenet-ng,


### modifying apps
#### frida
frida-trace ./{application} -i '*'
this will create files that hook into the functions that are being called
but it will hook into way to much

so use to find non default librarys
ldd ./{application}
fe and then use it in the trace:
frida-trace ./{application} -i 'libaocgame.so!*'

and we can add code to function to log all things that are used as arguments or retval:
onEnter:
log("args[0] "+ args[0]);
log("args[1] "+ args[1]);
log("args[2] "+ args[2]);
onLeave:
log("retval[0] "+ retval[0]);
log("retval[1] "+ retval[1]);
log("retval[2] "+ retval[2]);

in the on leave 
we can edit these return values:
args[0] = ptr(1337);
