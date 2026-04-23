from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.telegram import send_letter_to_telegram
from app.services.mail import send_letter_to_email
from app.schemas import Letter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/send-letter")
def send_letter(letter: Letter):
    errors = []
    try:
        send_letter_to_telegram(letter.name, letter.message, letter.contacts)
    except Exception as e:
        errors.append(f"telegram: {e}")
    try:
        send_letter_to_email(letter.name, letter.message, letter.contacts)
    except Exception as e:
        errors.append(f"email: {e}")
    if errors:
        raise HTTPException(status_code=500, detail=errors)
    return {"status": "sent"}
