import smtplib
import os


def send_mail(subject: str, massage: str) -> None:
    """
    Отправляет сообщение через gmail аккаунт
    Args:
        subject (str): Тема сообщения
        massage (str): Текст сообщения
    """
    # Настройки для подключения
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
        
    # Логин почты гугл. Пароль для приложения, который надо создать в аккаунте гугл
    login = 'djang5111@gmail.com'
    password = os.getenv('GMAIL_APP_PASS')
    
    # Залогиниться
    server.login(login, password)

    # Отправитель и Получатель
    sender = 'djang5111@gmail.com'
    receiver = 'lackroy511@gmail.com'

    # Тема сообщения и тело сообщения
    subject = subject
    message = massage

    # Формирование сообщения
    email = f'Subject: {subject}\n\n{message}'
    
    # Русский не поддерживается, поэтому энкодим
    email = email.encode("UTF-8")
    
    # Отправить сообщение
    server.sendmail(sender, receiver, email)

    # Дисконнект
    server.quit()

