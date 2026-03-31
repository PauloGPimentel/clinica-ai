from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Você é assistente de clínica médica.
Seu objetivo é agendar consultas via WhatsApp.

Regras:
- Seja educado e direto
- Faça uma pergunta por vez
- Conduza o paciente até finalizar o agendamento
"""

def responder(mensagem, historico):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += historico
    messages.append({"role": "user", "content": mensagem})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content
