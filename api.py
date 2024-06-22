from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import uvicorn

app = FastAPI()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    return None

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)