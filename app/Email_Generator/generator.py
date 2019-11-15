import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import requests


MY_ADDRESS = 'sistema.LosFiels@gmail.com'
PASSWORD = 'asdfghjkl1234567890'


def getUsers():
    res_get = requests.get('http://fiel.tk/membership/user/all')
    status, data = res_get.status_code, res_get.json()
    return data['users']

    
def read_template():
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    filename = "template.html"
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send(contract):
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    message_template = read_template()

    users = getUsers()

    print(users)

    for email in contract['emails']:
        subject = email['subject']
        content = email['content']

        
        for user in users:

            msg = MIMEMultipart('alternative')
            msg['From']=MY_ADDRESS
            msg['To']= user['user_email']
            msg['Subject']= subject

            plain_msg = content
            html_msg = message_template.substitute({'USERNAME': user['user_name'] , 'CONTENT': content})

            msg.attach(MIMEText(plain_msg, 'plain'))
            msg.attach(MIMEText(html_msg, 'html'))

            s.send_message(msg)
            del msg
    
    s.quit()
    
if __name__ == '__main__':
    send(
        {
            "emails":[
                {
                    "subject": "First Mail",
                    "content": "Vamos ha hacer maldades"
                },
                {
                    "subject": "Second Mail",
                    "content": "No para dale"
                }
            ]
        }
    )