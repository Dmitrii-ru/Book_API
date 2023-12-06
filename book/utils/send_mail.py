import smtplib
from email.mime.text import MIMEText
from test_book_app.settings import env


def send_wellcome_mail(obj):
    """
    Send mail
    """
    try:
        user_date = obj
        # Адрес отправки почты
        sender = env('EMAIL_SENSOR')
        # Пароль почты
        password = env('EMAIL_PASSWORD')
        # Хост почты
        email_host = env('EMAIL_HOST_NAME')
        # Порт
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


    except Exception as error:
        import logging
        logging.error(f"Произошла ошибка при отправке письма: {error}")
