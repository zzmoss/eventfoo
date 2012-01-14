import smtplib
from email.mime.text import MIMEText

def emailto(username = "internatrails@gmail.com",password="mambalam",you="internatrails@gmail.com", to=['madhuvishy@gmail.com','karthik.s.sundaram@gmail.com'], subject = "", content = "", attachmentimage = ""):
    HOST = 'smtp.gmail.com'
    PORT = 587

    server = smtplib.SMTP(HOST,PORT)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    
    for emailid in to:
        fp = open(content,'rb')
        msg = MIMEText(fp.read())
        fp.close()
        msg['Subject'] = subject
        msg['From'] = you
        msg['To'] = emailid
        server.sendmail(you,emailid,msg.as_string())

    #attachment doesn't work yet
