import smtplib
from email.mime.text import MIMEText
from app.config import EMAIL, EMAIL_PASSWORD, TO_EMAIL


def send_letter_to_email(name: str, message: str, contacts: str | None = None):
    text = f"""Новое письмо

Имя: {name}
Сообщение: {message}
Контакты: {contacts if contacts else 'не указаны'}
"""
    msg = MIMEText(text, "plain", "utf-8")
    msg["Subject"] = "Новое письмо"
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
