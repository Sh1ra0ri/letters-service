import requests
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_letter_to_telegram(name: str, message: str, contacts: str | None = None):
    text = f"""Новое письмо

Имя: {name}
Сообщение: {message}
Контакты: {contacts}
"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.post(
        url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text}, timeout=5
    )
    response.raise_for_status()
