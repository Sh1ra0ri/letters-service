from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

class Letter(BaseModel):
    name: str
    message: str

@app.post("/send-letter")
def send_letter(letter: Letter):
    return {"received": letter}
