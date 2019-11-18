PLEASE READ!

This is my first code and first upload to github. please be kind.

This code will convert pdfs, epubs and rars into .mobi files and send them directly to your kindle.
you will need to install https://calibre-ebook.com for this to work.
in the code you will need to change a few lines to make sure it sends to your kindle.
line 7
line 103
line 104
line 105

For line 7, I suggest a folder on your desktop called "Books". Remember to finish your path with /
example: /Users/yournamehere/Desktop/Books/
If in the created folder you create a subfolder named "Kindle", you may delete line 8 and line 156.
The Kindle folder is created to store the converted files and is deleted once the folder is empty.

For line 103, when entering an email address, use a google email and set "Allow less secure Apps" to ON. 
This is important.

Line 55 is set if you install calibre on a macOS. 
Otherwise you will need to locate & change the path for the file /ebook-convert

The code will only recognize .pdf .epub .rar and .mobi as files, everything else it will not see.

to find your kindle address, see https://www.amazon.com/gp/sendtokindle/email

The code will loop through all books until they are all converted, and then send all to kindle as single emails.
If the files are too big, it will not send. It may not be the cleanest of codes, but I am happy with the outcome.

not sure where to get ebooks from? I suggest to give this a read
https://www.reddit.com/r/Piracy/comments/2oftbu/guide_the_idiot_proof_guide_to_downloading_ebooks/


once all is set, call the code in terminal by finding its directory and typing
python kindsend.py

HAPPY READING!

