from PyPDF2 import PdfReader

async def read_file(file):
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        content = await file.read()
        return content.decode("utf-8")

    if filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    return ""
