import smtplib
from email.mime.text import MIMEText
from test_book_app.settings import env
import json


def send_wellcome_mail(obj):
    try:
        user_date = obj
        sender = env('EMAIL_SENSOR')
        password = env('EMAIL_PASSWORD')
        email_host = env('EMAIL_HOST_NAME')
        port = env('EMAIL_PORT')

        server = smtplib.SMTP(email_host, port)

        server.starttls()
        to_send = user_date['email']

        msg = MIMEText(f"Приветствую  Вас {user_date['username']}")
        msg['To'] = to_send
        msg['From'] = sender
        msg['Subject'] = 'Добро пожаловать'

        server.login(sender, password)
        server.sendmail(sender, to_send, msg.as_string())
        print("send_wellcome_mail")

    except Exception as error:
        pass
