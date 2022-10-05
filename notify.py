
# Import smtplib for the actual sending function
from email import message_from_bytes
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

import os
from dotenv import load_dotenv
load_dotenv()

import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

receiver_email = os.getenv('EMAIL')  # Enter receiver address
password = os.getenv('PASSWORD')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
sender = os.getenv('SENDER')

def send_email():
    data = [["Reddit", "Astrophysicist", "Redditor"], ["Google", "Googler", "Programmer"]]

    my_sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

    from_email = Email(sender)  
    to_email = To(receiver_email)  

    subject = "Company Updates"
    
    message = ""
    ln = "\n"
    indent = '    '
    for company in data:
        message += company[0] + ln
        for i,job in enumerate(company):
           if i>=1:
            message += indent + "- " + job + ln
     
    # print("m: " + message)
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = my_sg.client.mail.send.post(request_body=mail_json)
    
    
    # # Create a text/plain message
    # msg = EmailMessage()
    
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    
    # msg.set_content(message)
    # msg['Subject'] = "Update"
    # msg['From'] = "gordon.site.mailing@gmail.com"
    # msg['To'] = receiver_email

    # # Send the message via our own SMTP server.
    # # s = smtplib.SMTP('localhost')
    # s = smtplib.SMTP('localhost', 1025)
    # # s.send_message(msg)
    # s.sendmail("gordon.site.mailing@gmail.com", receiver_email, message)
    # s.quit()
    
    
    
    
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