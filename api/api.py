from fastapi import FastAPI,UploadFile,File
from fastapi.responses import RedirectResponse
from utils.utils import read_file
import os

app = FastAPI()

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    content = await file.read()
    
    return read_file(content,extension=os.path.splitext(file.filename)[1].lower())