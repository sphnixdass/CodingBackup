import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
html = """\
<html>
  <body>
    <p>Hi,<br>
       Intruder has been dected!!!!<br>
    </p>
    <img id="img" src="http://183.82.36.26:5010/static/43.jpg" style="border: 3px solid black">
  </body>
</html>
"""


#The mail addresses and password
sender_address = 'sphnixdass@gmail.com'
sender_pass = 'tailoymewuzueuri'
receiver_address = ['sphnixdass@gmail.com', 'carolin.s@kotak.com', 'selvgnb@natwest.com', 'carolins82@gmail.com']
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = ", ".join(receiver_address)
message['Subject'] = 'Intruder alert!!!.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(html, 'html'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')