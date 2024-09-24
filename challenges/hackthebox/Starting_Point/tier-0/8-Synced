scanning this box shows us a rsync service

this shows us the shares
rsync -avz list-only rsync://{boxip}/

and we can sync it locally:
rsync -avz rsync://{boxip}/public ./testpublic

and then can get the flag:
cd testpublic
ls
cat flag.txt