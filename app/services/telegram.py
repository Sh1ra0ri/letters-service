import requests
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_letter_to_telegram(name: str, message: str, contacts: str | None = None):
    text = f"""Новое письмо

Имя: {name}
Сообщение: {message}
Контакты: {contacts if contacts else 'не указаны'}
"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text})
