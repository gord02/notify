# environment variables 
import os
from dotenv import load_dotenv
load_dotenv()

import sendgrid
from email.message import EmailMessage
from sendgrid.helpers.mail import Mail, Email, To, Content

receiver_email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
sender = os.getenv('SENDER')

def send_email(data):
    print("data: ", data)
    # data = [["Reddit", "Astrophysicist", "Redditor"], ["Google", "Googler", "Programmer"]]

    send_grid = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

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
     
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    send_grid.client.mail.send.post(request_body=mail_json)
    