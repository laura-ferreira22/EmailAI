import os
from openai import OpenAI

def generate_response(text: str, categoria: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "Recebemos seu email e em breve retornaremos."

    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""
Você é um assistente corporativo de uma empresa financeira.

Classificação do email: {categoria}

Email recebido:
{text}

Gere uma resposta educada, clara e profissional.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Erro OpenAI:", e)
        return "Recebemos seu email e em breve retornaremos."
