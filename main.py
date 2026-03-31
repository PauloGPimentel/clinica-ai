from fastapi import FastAPI, Request
from agent import responder

app = FastAPI()

memoria = {}

@app.get("/")
def home():
    return {"status": "rodando"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    numero = data.get("from", "teste")
    mensagem = data.get("message", "")

    if numero not in memoria:
        memoria[numero] = []

    resposta = responder(mensagem, memoria[numero])

    memoria[numero].append({"role": "user", "content": mensagem})
    memoria[numero].append({"role": "assistant", "content": resposta})

    return {"reply": resposta}
