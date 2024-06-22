from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import uvicorn
from main import PdfSummarizer

app = FastAPI()
pdf_summarizer = PdfSummarizer()

@app.post("/Pdf-Summarizer/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        file_location = f"temp/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        
        with open(file_location, "wb") as f:
            f.write(await file.read())
            
        pdf_summary = pdf_summarizer.get_response_llm(pdf=file_location)
        
        os.remove(file_location)
        
        if pdf_summary is None:
                return JSONResponse(content={"message": "Erro ao processar o PDF"}, status_code=500)

        return JSONResponse(content={"summary": pdf_summary}, status_code=200)
    except Exception as e:
        print(f"ERROR: {e}")
        return JSONResponse(content={"message": "Erro no servidor"}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)