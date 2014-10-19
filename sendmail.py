
# simple email message library
import smtplib

# for mime messages
from  email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# package for fetching data from clipboard
import pyperclip

# function for sending email
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com'): 
		"""Function for connecting, authenticating , sending mail and quitting from smtp server """
		
		server = smtplib.SMTP()
		server.connect(smtpserver)
		server.starttls()
		server.login(login,password)
		problems = server.sendmail(from_addr, to_addr_list, message.as_string())
		server.quit()
		return problems
    
# Taking required inputs
username = raw_input("Enter Username!")
password = raw_input("Enter Password!")
to_addr = raw_input("Enter To Address")
cc_addr = raw_input("Enter CC Address")
subject = raw_input("Enter Subject!")
message = pyperclip.getcb().strip()
if(len(message)==0)
message = raw_input("Enter Message!")
_attachment = raw_input("Full name of the attachment! (assumes file is in current directory)") or 'image.jpg'

#Preparing mime message
mime_message = MIMEMultipart()

"""# Converting simple text to mime text and adding it to mime message
mime_text= MIMEText(message)
mime_message.attach(mime_text)"""

# Adding html content(image) to mime message
msgText = MIMEText('<b>'+message+'</b><br><img src="cid:'+_attachment+'"><br>', 'html')
mime_message.attach(msgText)

# Adding image as attachment
f = open(_attachment,"rb")
mime_image = MIMEImage(f.read())
f.close()
mime_image.add_header("Content-ID",_attachment)
mime_message.attach(mime_image)

# Adding sender and receiver to mime message
mime_message["To"] = to_addr
mime_message["From"] = ''
mime_message["Subject"] = subject
    
# Sending mime message
sendemail(from_addr    = '', 
          to_addr_list = [to_addr],
          cc_addr_list = [cc_addr], 
          subject      = subject, 
          message      = mime_message, 
          login        = username, 
          password     = password)   
