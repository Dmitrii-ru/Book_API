import smtplib
from email.mime.text import MIMEText
import json


def send_wellcome_mail(obj):
    try:
        user_date = obj
        sender = 'testemailru014@gmail.com'
        password = 'jiwmpeflbdfrqold'
        email_host = 'smtp.gmail.com'
        port = 587

        server = smtplib.SMTP(email_host, port)


        server.starttls()
        to_send = user_date['email']

        msg = MIMEText(f"Приветствую  Вас {user_date['username']}")
        msg['To'] = to_send
        msg['From'] = sender
        msg['Subject'] = 'Добро пожаловать'

        server.login(sender, password)
        server.sendmail(sender, to_send, msg.as_string())

    except Exception as error:
        pass