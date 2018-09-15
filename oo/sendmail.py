import smtplib
from email.mime.text import MIMEText

SMTPServer = "smtp.163.com"
Sender = "djlove986@163.com"
passwd = "Password1"  # client authentication code

message = "hello,this is a doc "
msg = MIMEText(message)  # convert to mail text

msg["Subject"] = "hello,me"
msg["From"] = Sender
mailServer = smtplib.SMTP(SMTPServer, 25)  # create smtp server
mailServer.login(Sender, passwd)
mailServer.sendmail(Sender, ["345141067@qq.com"], msg.as_string())
mailServer.quit()
