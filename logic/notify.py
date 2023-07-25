# environment variables 
import os
from dotenv import load_dotenv
load_dotenv()

import sendgrid
from email.message import EmailMessage
from sendgrid.helpers.mail import Mail, Email, To, Content

# import hyperlink

receiver_email = os.getenv('EMAIL')
# password = os.getenv('PASSWORD')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
sender = os.getenv('SENDER')

def send_email(data):
    # print("data: ", data)
    send_grid = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

    from_email = Email(sender)  
    to_email = To(receiver_email)  

    subject = "Company Updates"
    
    message = ""
    ln = "\n"
    indent = '    '

    for company in data:
        company[0] = company[0].capitalize()
        link = company[1]
        # url = hyperlink.parse(link)
        # linkStr = f"Link: {url}" 
        
        message += company[0] + ln
        message += link+ ln
        # message += linkStr + ln
        # message += url + ln
        
        for i,job in enumerate(company):
           if i>=2:
            message += indent + "- " + job + ln 
        message += ln
    # print(message)
    
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    send_grid.client.mail.send.post(request_body=mail_json)
    
def parsing_error(company):
    send_grid = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    from_email = Email(sender)  
    to_email = To(receiver_email)  

    subject = "Scrapping Error"
    
    message = f"Error scrapping company {company}"
    print(f"Error scrapping company {company}")
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    # commented out line since errors aren't important
    # send_grid.client.mail.send.post(request_body=mail_json)
    
def test_email():
    send_grid = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

    from_email = Email(sender)  
    to_email = To(receiver_email)  

    subject = "Company Updates"
    
    message = "This is test message "
     
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    send_grid.client.mail.send.post(request_body=mail_json)
    
# send_email([["Google", "SWE"], ["reddit", "SWE"]])

# test_email()