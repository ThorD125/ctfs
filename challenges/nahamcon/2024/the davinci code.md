opening the site shows us a link to /code

this shows us some stackcode and we can open each to see some paths and methods to use

using the methhod propfind and url:`${URL}/`
it results int he xml of the main directory

going to multiple of these i found a backup of the app file
`${URL}/static/app.py.backup`

i found the location of the file `${URL}/the_secret_dav_inci_code/flag.txt`
but couldnt open it

looking further into the `app.py.backup` file
i found there also is a `move` method i could use

together with a header: `Destination`

playing around with it, and after figuring it out:

and figuring out, the stackcode had the error: `failed to get the code.html template`

i tried:
method: `MOVE`
url: `${URL}/the_secret_dav_inci_code/flag.txt`
header: `Destination: /templates/code.html`

and then i could access the `${URL}/code` to get the flag