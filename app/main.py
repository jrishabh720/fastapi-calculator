from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalculatorRequest(BaseModel):
    a: int
    b: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/calculate")
def calculate(request: CalculatorRequest):
    return {
        "result": request.a + request.b
    }