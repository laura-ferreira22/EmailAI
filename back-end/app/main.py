from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware


from app.services.responder import classify_and_generate_response
from app.utils.file_reader import read_file

app = FastAPI(title="EmailAI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   
        "https://emailai.vercel.app"  
    ],
    allow_credentials=True,
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

    

    result = classify_and_generate_response(content)
    return result


