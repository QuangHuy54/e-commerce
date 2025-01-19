from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controllers import user

app = FastAPI()

app.include_router(user.router, prefix="/api")
app.mount("/", StaticFiles(directory="files"), name="files")
