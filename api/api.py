from fastapi import FastAPI,UploadFile,File,status,Form
from fastapi.responses import RedirectResponse
from .utils.utils import create_metadata
from models.models import ChunkingStrategy
app = FastAPI()

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(chunk_size: int, chunk_strat:ChunkingStrategy=Form(...), file: UploadFile = File(...)):
    content = await file.read()
    file_name = file.filename
    filename, extension = file_name.split(".")[0], file_name.split(".")[1]
    create_metadata(content, extension=extension, filename=filename,chunk_size=chunk_size,chunk_strat=chunk_strat.lower())
    return {"status":status.HTTP_200_OK,"message":"File upload sucessfull"}
