import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://emailia.app",
    "X-Title": "EmailIA"
}

def classify_and_generate_response(text: str) -> dict:
    if not OPENROUTER_API_KEY:
        return {
            "categoria": "Improdutivo",
            "resposta": "Recebemos seu email e em breve retornaremos."
        }

    try:
        prompt = f"""
Você é um assistente corporativo de uma empresa do setor financeiro.

Analise o email abaixo.

Primeiro, diga APENAS uma palavra na primeira linha:
Produtivo ou Improdutivo

Depois, em um novo parágrafo, escreva apenas a resposta profissional
ao email, sem títulos, sem JSON, sem explicações extras.

Email:
{text}
"""

        payload = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 300
        }

        response = requests.post(
            OPENROUTER_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        content = data["choices"][0]["message"]["content"].strip()

        # ---- PROCESSAMENTO DA RESPOSTA ----
        lines = content.split("\n", 1)

        categoria = lines[0].strip()

        if categoria not in ["Produtivo", "Improdutivo"]:
            categoria = "Improdutivo"

        resposta = lines[1].strip() if len(lines) > 1 else ""

        return {
            "categoria": categoria,
            "resposta": resposta
        }

    except Exception as e:
        print("Erro OpenRouter:", e)
        return {
            "categoria": "Improdutivo",
            "resposta": "Agradecemos sua mensagem. Em breve retornaremos."
        }
