from fastapi import FastAPI
import os

__version__ = "1.0.0"

app = FastAPI()

@app.get("/version")
async def get_version():
    return {"version": __version__}

@app.get("/exit")
async def exit_app():
    os._exit(0)

@app.get("/error")
async def error_app():
    os._exit(1)