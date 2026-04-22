from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.telegram import send_letter_to_telegram
from app.services.mail import send_letter_to_email
from app.schemas import Letter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/send-letter")
def send_letter(letter: Letter):
    send_letter_to_telegram(letter.name, letter.message, letter.contacts)
    send_letter_to_email(letter.name, letter.message, letter.contacts)
    return {"status": "sent"}
