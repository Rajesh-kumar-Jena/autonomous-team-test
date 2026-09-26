from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

app = FastAPI(title="Calculator API")

class AddRequest(BaseModel):
    a: float
    b: float

@app.post("/api/v1/add")
def add_numbers(payload: AddRequest):
    result = payload.a + payload.b
    return {"result": result}

@app.get("/")
def read_root():
    if os.path.exists("public/index.html"):
        return FileResponse("public/index.html")
    return {"message": "Calculator API"}

if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")
