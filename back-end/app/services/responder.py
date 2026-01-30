import os
from openai import OpenAI

def generate_response_and_category(text: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return {
            "categoria": "Improdutivo",
            "resposta": "Recebemos seu email e em breve retornaremos."
        }

    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""
Você é um assistente corporativo de uma empresa do setor financeiro.

Analise o email abaixo e:
1. Classifique como APENAS uma das opções:
   - Produtivo (requer ação, resposta ou acompanhamento)
   - Improdutivo (não requer ação imediata)

2. Gere uma resposta curta, educada e profissional,
adequada à classificação.

Email:
{text}

Retorne exatamente no seguinte formato JSON:
{{
  "categoria": "Produtivo ou Improdutivo",
  "resposta": "texto da resposta"
}}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        content = response.choices[0].message.content

        # segurança mínima
        if "Produtivo" in content:
            categoria = "Produtivo"
        else:
            categoria = "Improdutivo"

        return {
            "categoria": categoria,
            "resposta": content
        }

    except Exception as e:
        print("Erro OpenAI:", e)
        return {
            "categoria": "Improdutivo",
            "resposta": "Recebemos seu email e em breve retornaremos."
        }
