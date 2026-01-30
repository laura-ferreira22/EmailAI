import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(text: str, categoria: str) -> str:
    prompt = f"""
Você é um assistente corporativo de uma empresa financeira.

Classificação do email: {categoria}

Email recebido:
{text}

Gere uma resposta educada, clara e profissional,
adequada ao contexto corporativo.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
