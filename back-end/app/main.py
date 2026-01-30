from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from app.services.classifier import classify_email
from app.services.responder import generate_response
from app.utils.file_reader import read_file


app = FastAPI(title="EmailIA API")

# CORS (liberar para o front depois)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois troque pela URL do Vercel
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-email")
async def process_email(
    text: str = Form(None),
    file: UploadFile = File(None)
):
    if not text and not file:
        return {"error": "Nenhum conteúdo enviado"}

    content = text if text else await read_file(file)

    categoria = classify_email(content)
    resposta = generate_response(content, categoria)

    return {
        "categoria": categoria,
        "resposta": resposta
    }
