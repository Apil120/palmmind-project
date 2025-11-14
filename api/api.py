from fastapi import FastAPI,UploadFile
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(file:UploadFile):
    ...