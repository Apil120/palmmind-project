from fastapi import FastAPI,UploadFile,File,status
from fastapi.responses import RedirectResponse
from .utils.utils import save_file

app = FastAPI()

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    content = await file.read()
    file_name = file.filename
    filename, extension = file_name.split(".")[0], file_name.split(".")[1]
    save_file(content,extension=extension,filename=filename)
    return status.HTTP_200_OK
