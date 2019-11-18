#user input version

import subprocess
import os
from pathlib import Path

folder = ## path to the folder that holds all books
os.mkdir(folder + "Kindle/")
    
# finds the number of books stored. if 0 books, the conversion will not run
def book_shelf():
    books = []
    for filename in os.listdir(folder):
        if filename.endswith(".epub"):
            epub = filename[:-len(".epub")]
            books.append(epub)
        elif filename.endswith(".rar"):
            rar = filename[:-len(".rar")]
            books.append(rar)
        elif filename.endswith(".mobi"):
            os.rename(folder + filename, folder + "Kindle/" + filename)
            print ("Moved" + filename + "\n")
        elif filename.endswith(".pdf"):
            pdf = filename[:-len(".pdf")]
            books.append(pdf)
        else:
            pass            
    return len(books)
    
# returns the name of one book in books that will be processed for conversion
def book():
    files = []
    for filename in os.listdir(folder):
        if filename.endswith(".epub"):
            epub = filename
            files.append(epub)           
        elif filename.endswith(".rar"):
            rar = filename
            files.append(rar)           
        elif filename.endswith(".mobi"):
            mobi = filename
            files.append(mobi)
        elif filename.endswith(".pdf"):
            pdf = filename
            files.append(pdf)
    while len(files) > 0:
        return files[0]
    else:
        files = "Empty"
        return files

# converts the chosen book to the correct file, deletes the orginal file
# places new file into a subfolder, ready to be sent
def convert():
    call = '/Applications/calibre.app/Contents/MacOS/ebook-convert '   
    folder_out = folder + ("Kindle/")  
    for files in book():
        if book() == "Empty":
            return book()
        else:
            book_in = folder + book()
            book_out = folder + "Kindle/" + book()[:-4] + (".mobi")
            final = call + " '" + book_in + "' '" + book_out + "' " 
            os.system(final)   
            print("\n", book(),"converted and original deleted\n")
            os.remove(book_in)

# loops the convert process until there are no more books to convert
def run_convert():
    while book_shelf() > 0:
        convert()
        continue
        if book_shelf() == 0:
            break
    else:
        print("No more books to convert. Sending all Files to Kindle. \n")

run_convert()

# returns a book ready to be sent, if there is no book. returns nothing
def first_send():
    send = []
    for mobi in os.listdir(folder + "Kindle/"):
        if mobi.endswith(".mobi"):
            send.append(mobi)
        else:
            pass
    for file in os.listdir(folder + "Kindle/"):
        if file != file.endswith(".mobi"):
            send.append("No Mobis Found")          
    return send[0]

# packages book to email and sends
def send_to_kindle():

    print("sending " + first_send())
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import os.path
    email = ## your email address to send files from
    password = ## the password of your email address
    send_to_email = ## the address of your kindles email
    subject = first_send()
    message = first_send() + (" Sent to Kindle")
    file_location = folder + "Kindle/" + first_send()
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    # Setup the attachment
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()   
    print("Sent " + first_send())
    print("Removed " + first_send())
    os.remove(file_location)

# returns value of books to send. if 0, will not send anything
def booklist():
    shelf = []
    for filename in os.listdir(folder + "Kindle/"):
        if filename.endswith(".mobi"):
            mobi = filename[:-len(".mobi")]
            shelf.append(mobi)
        else:
            pass        
    return len(shelf)

# if there are books to send, it will loop process until all sent.
def send_it():
    while booklist() > 0:
        send_to_kindle()
        continue
        if booklist() == 0:
            break
    else:
    	print("\nNo more books to send.\n")


send_it()
os.rmdir(folder + "Kindle/")


