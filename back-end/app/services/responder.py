import os
import requests

HF_TOKEN = os.getenv("HF_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

CLASSIFIER_URL = (
    "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
)

GENERATOR_URL = (
    "https://api-inference.huggingface.co/models/google/flan-t5-base"
)


def classify_and_generate_response(text: str) -> dict:
    try:
        
        classification_payload = {
            "inputs": text,
            "parameters": {
                "candidate_labels": ["Produtivo", "Improdutivo"]
            }
        }

        class_response = requests.post(
            CLASSIFIER_URL,
            headers=HEADERS,
            json=classification_payload,
            timeout=20
        )
        class_response.raise_for_status()
        class_data = class_response.json()

        categoria = class_data["labels"][0]

       
        if categoria == "Produtivo":
            prompt = (
                "Você é um assistente corporativo. "
                "Gere uma resposta profissional e objetiva para o email abaixo, "
                "indicando que a solicitação será analisada:\n\n"
                f"{text}"
            )
        else:
            prompt = (
                "Você é um assistente corporativo. "
                "Gere uma resposta educada e curta para o email abaixo, "
                "sem indicar necessidade de ação:\n\n"
                f"{text}"
            )

        gen_payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 120
            }
        }

        gen_response = requests.post(
            GENERATOR_URL,
            headers=HEADERS,
            json=gen_payload,
            timeout=20
        )
        gen_response.raise_for_status()
        gen_data = gen_response.json()

        resposta = gen_data[0]["generated_text"]

        return {
            "categoria": categoria,
            "resposta": resposta
        }

    except Exception as e:
        print("Erro Hugging Face:", e)

       
        return {
            "categoria": "Improdutivo",
            "resposta": (
                "Agradecemos sua mensagem. "
                "Caso precise de algo mais, ficamos à disposição."
            )
        }
