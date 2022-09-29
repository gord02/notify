
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

import os
from dotenv import load_dotenv
load_dotenv()

receiver_email = os.getenv('EMAIL')  # Enter receiver address
password = os.getenv('PASSWORD')


def send_email():

    # Create a text/plain message
    msg = EmailMessage()
    
    message = """\
    Subject: Hi there

    This message is sent from Python."""
    
    msg.set_content(message)
    msg['Subject'] = "Update"
    msg['From'] = "gordon.site.mailing@gmail.com"
    msg['To'] = receiver_email

    # Send the message via our own SMTP server.
    # s = smtplib.SMTP('localhost')
    s = smtplib.SMTP('localhost', 1025)
    # s.send_message(msg)
    s.sendmail("gordon.site.mailing@gmail.com", receiver_email, message)
    s.quit()
    
    
    
    
    # # port = 465  # For SSL
    # # smtp_server = "smtp.gmail.com"
    # smtp_server = "smtp.gmail.com"
    # port = 587  # For starttls
    # sender_email = "" 
    
  
    
   

    # # context = ssl.create_default_context()
    # # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    # #     server.login(sender_email, password)
    # #     server.sendmail(sender_email, receiver_email, message)
    # # Create a secure SSL context
    # context = ssl.create_default_context()

    # # Try to log in to server and send email
    # try:
    #     server = smtplib.SMTP(smtp_server,port)
    #     server.ehlo() # Can be omitted
    #     server.starttls(context=context) # Secure the connection
    #     server.ehlo() # Can be omitted
    #     server.login(sender_email, password)
    #     # TODO: Send email here
    # except Exception as e:
    #     # Print any error messages to stdout
    #     print(e)
    # finally:
    #     server.quit() 
send_email()