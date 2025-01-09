# this:
is a bit of a guide into reversing and exploiting apps

## what the binary
magicbytes are the first x bytes that can help you determine what kynd of file it is fe a picture an executable etc

## before doing anything
get the filehash
and make a copy, and use the copy to work with

## windows exes
peheaders contain a lot of info, "pe studio" allows you to look at these

## decompiling
ilspy: .net

## frida modifying apps
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
