# cryptography

## AES Attacking ECB Oracles

chosen plain text attacks
trying payload fe A

we check how many we had to insert
until we see a second block being added (save this amount)
then count until we get a 3 block (save this amount)
then we substract the first from the last to get the length of a block

then after this we insert 2blocks of the A character
then we prepend this with a B character
and add more until we see 2 blocks being the same
this determines the offsett

so we insert the offsett B's
and 1 full block of A's then remove 1 A
this gives us a reference of what it looks when its "correct"
so now we can bruteforce the key.
and so we can continue to bruteforce the full key


