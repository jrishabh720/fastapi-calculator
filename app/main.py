from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/")
def home():
    return FileResponse("app/static/index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/calculate")
def calculate(request: CalculatorRequest):

    if request.operation == "add":
        result = request.a + request.b

    elif request.operation == "subtract":
        result = request.a - request.b

    elif request.operation == "multiply":
        result = request.a * request.b

    elif request.operation == "divide":
        if request.b == 0:
            return {"error": "Cannot divide by zero"}
        result = request.a / request.b

    else:
        return {"error": "Invalid operation"}

    return {
        "result": result
    }