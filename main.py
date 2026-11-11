from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Calculator API", version="1.0.0")


class CalculationRequest(BaseModel):
    a: float
    b: float


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/add")
def add_numbers(request: CalculationRequest):
    return {"result": request.a + request.b}


@app.post("/subtract")
def subtract_numbers(request: CalculationRequest):
    return {"result": request.a - request.b}


@app.post("/multiply")
def multiply_numbers(request: CalculationRequest):
    return {"result": request.a * request.b}
