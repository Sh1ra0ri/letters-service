# Letters Service

Сервис для отправки писем читателей в Telegram-чат редакции и на email.

## Стек

- Python 3.11+
- FastAPI
- smtplib (Gmail SMTP)
- Telegram Bot API

## Установка

1. Клонируй репозиторий:
```bash
   git clone https://github.com/Sh1ra0ri/letters-service
   cd letters-service
```

2. Создай виртуальное окружение и активируй его:
```bash
   python -m venv .venv
   .venv\Scripts\activate
```

3. Установи зависимости:
```bash
   pip install -r requirements.txt
```

4. Создай `.env` файл по примеру `.env.example`:
```bash
   copy .env.example .env
```

5. Заполни `.env` своими данными.

## Переменные окружения

| Переменная | Описание |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Токен бота от @BotFather |
| `TELEGRAM_CHAT_ID` | ID чата редакции |
| `EMAIL` | Gmail с которого отправляются письма |
| `EMAIL_PASSWORD` | Пароль приложения Gmail |
| `TO_EMAIL` | Email редакции куда приходят письма |

### Как получить Telegram Bot Token
1. Открой @BotFather в Telegram
2. Напиши `/newbot`
3. Следуй инструкциям — получишь токен

### Как получить Telegram Chat ID
1. Добавь бота в чат редакции
2. Напиши любое сообщение в чат
3. Открой в браузере: `https://api.telegram.org/bot<TOKEN>/getUpdates`
4. Найди поле `chat.id`

### Как получить пароль приложения Gmail
1. Включи двухфакторную аутентификацию на аккаунте Google
2. Перейди на myaccount.google.com/apppasswords
3. Создай новый пароль — скопируй 16 символов без пробелов

## Запуск

Локально:
```bash
uvicorn app.main:app --reload
```

С доступом для фронтенда:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API

### POST /send-letter

Отправляет письмо в Telegram и на email.

**Тело запроса:**
```json
{
  "name": "Имя отправителя",
  "message": "Текст сообщения",
  "contacts": "@username или null"
}
```

**Ответ:**
```json
{
  "status": "sent"
}
```

**Пример fetch:**
```javascript
fetch("http://localhost:8000/send-letter", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    name: "Имя",
    message: "Сообщение",
    contacts: "@username"
  })
})
```