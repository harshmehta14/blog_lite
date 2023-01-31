import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from jinja2 import Template


SMPTP_SERVER_HOST = "localhost"
SMPTP_SERVER_PORT = 1025
SENDER_ADDRESS ="email@bloglite.com"
SENDER_PASSWORD =""


def send_email(to_address,subject,message,content="text",attachment_file=None):
    try:
        print("Sending Email")
        msg = MIMEMultipart()
        msg['From']= SENDER_ADDRESS
        msg['To']= to_address
        msg['Subject']= subject
        
        if content == "html":
            msg.attach(MIMEText(message,'html'))
        else:
            msg.attach(MIMEText(message, 'plain'))

        if attachment_file:
            with open(attachment_file,"rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment: filename={attachment}")
            msg.attach(part)   

        s= smtplib.SMTP(host=SMPTP_SERVER_HOST,port=SMPTP_SERVER_PORT)
        s.login(SENDER_ADDRESS,SENDER_PASSWORD)
        s.send_message(msg)
        s.quit()
        print("Email Sent")
        return "Email Sent Succefully"
    except Exception as e:
        print(e)

def write():
    f = open("demofile2.txt", "w")
    f.write("Now the file has more content!")
    f.close()


# def send_email(to_address,subject,message,content="text",attachment=None):
#     msg = MIMEMultipart()
#     msg['To']=to_address
#     msg['From']=SENDER_ADDRESS
#     msg['Subject']=subject
#     if content == "html":
#         msg.attach(MIMEText(message,'html'))
#     else:
#         msg.attach(MIMEText(message, 'plain'))

#     if attachment:
#         with open(attachment,"rb") as a:
#             part = MIMEBase("application", "octet-stream")
#             part.set_payload(a.read())
#         encoders.encode_base64(part)
#         part.add_header("Content-Disposition", f"attachment: filename={attachment}")
#         msg.attach(part)          

#     s = smtplib.SMTP(host=SERVER_SMTP_HOST, port=SERVER_SMTP_PORT )
#     s.login(SENDER_ADDRESS,SENDER_PASSWORD)
#     s.send_message(msg)
#     s.quit()
#     return True