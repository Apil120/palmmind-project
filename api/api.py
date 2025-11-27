from fastapi import FastAPI,UploadFile,File,status
from fastapi.responses import RedirectResponse
from .utils.utils import create_metadata

app = FastAPI()

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    content = await file.read()
    file_name = file.filename
    filename, extension = file_name.split(".")[0], file_name.split(".")[1]
    create_metadata(content, extension=extension, filename=filename)
    return {"status":status.HTTP_200_OK,"message":"File upload sucessfull"}
