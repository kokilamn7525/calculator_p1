from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Addition API", version="1.0.0")


class AdditionRequest(BaseModel):
    a: float
    b: float


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/add")
def add_numbers(request: AdditionRequest):
    return {"result": request.a + request.b}
