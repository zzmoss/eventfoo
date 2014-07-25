import smtplib
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email import Encoders

def emailto(username = "internatrails@gmail.com",password="mambalam",you="internatrails@gmail.com", to=['madhuvishy@gmail.com','karthik.s.sundaram@gmail.com'], subject = "", content = "", imagedir = "", imagefile = ""):
    HOST = 'smtp.gmail.com'
    PORT = 587

    server = smtplib.SMTP(HOST,PORT)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    
    for emailid in to:
        msg = MIMEMultipart()
        fp = open(content,'rb')
        text = MIMEText(fp.read())
        fp.close()
        
        #imagedir should have trailing /
        fimg = open(imagedir+imagefile,'rb')
        img = MIMEBase('application','octet-stream')
        img.set_payload(fimg.read())
        Encoders.encode_base64(img)
        img.add_header('Content-Disposition','attachment',filename=imagefile)

        msg['Subject'] = subject
        msg['From'] = you
        msg['To'] = emailid
        msg.attach(text)
        msg.attach(img)

        server.sendmail(you, emailid, msg.as_string())

    #attachment doesn't work yet
