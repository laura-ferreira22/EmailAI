import os
from openai import OpenAI

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY não configurada")

    return OpenAI(api_key=api_key)


def generate_response(email_text: str):
    client = get_openai_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente que classifica emails como Produtivo ou Improdutivo e sugere uma resposta educada."
            },
            {
                "role": "user",
                "content": email_text
            }
        ]
    )

    return {
        "categoria": "Produtivo",  
        "resposta": response.choices[0].message.content
    }
