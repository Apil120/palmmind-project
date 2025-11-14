from fastapi import FastAPI,UploadFile,File
from fastapi.responses import RedirectResponse
from pdfminer.high_level import extract_text
import os

app = FastAPI()

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    content = await file.read()
    with open ("temp.pdf","wb") as temp_file:
        temp_file.write(content)
    
    data_json = {"text":extract_text("temp.pdf")}
    os.remove(path=os.getcwd()+"\\temp.pdf")
    return data_json
