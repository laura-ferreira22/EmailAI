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
Você é um assistente corporativo.

Analise o email abaixo e:
1. Classifique como APENAS uma das opções:
   - Produtivo (requer ação)
   - Improdutivo (não requer ação)

2. Gere uma resposta curta, educada e profissional,
adequada à classificação.

Email:
{text}

Retorne no formato JSON:
{{
  "categoria": "Produtivo ou Improdutivo",
  "resposta": "texto da resposta"
}}
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

        content = data["choices"][0]["message"]["content"]

        
        import json
        try:
            result = json.loads(content)
            return result
        except:
           
            categoria = "Produtivo" if "Produtivo" in content else "Improdutivo"
            return {
                "categoria": categoria,
                "resposta": content
            }

    except Exception as e:
        print("Erro OpenRouter:", e)
        return {
            "categoria": "Improdutivo",
            "resposta": "Agradecemos sua mensagem. Em breve retornaremos."
        }
