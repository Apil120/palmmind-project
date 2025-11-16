from fastapi import FastAPI,UploadFile,File
from fastapi.responses import RedirectResponse
from utils.utils import read_file,get_metadata
import os

app = FastAPI()

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    content = await file.read()
    extension = file.content_type.split("/")[1]
    return read_file(content,extension=extension)