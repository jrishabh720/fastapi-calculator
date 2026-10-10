from enum import Enum

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


# 1. Define permitted operations
class Operation(str, Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


# 2. Define the request model
class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: Operation


# 3. Define the response model
class CalculatorResponse(BaseModel):
    result: float


# 4. Home page
@app.get("/")
def home():
    return FileResponse("app/static/index.html")


# 5. Health check
@app.get("/health")
def health():
    return {"status": "ok"}


# 6. Calculator endpoint
@app.post(
    "/calculate",
    response_model=CalculatorResponse
)
def calculate(request: CalculatorRequest):

    if request.operation == Operation.ADD:
        result = request.a + request.b

    elif request.operation == Operation.SUBTRACT:
        result = request.a - request.b

    elif request.operation == Operation.MULTIPLY:
        result = request.a * request.b

    elif request.operation == Operation.DIVIDE:

        if request.b == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero"
            )

        result = request.a / request.b

    else:
        # Defensive fallback; the Enum rejects unsupported values.
        raise HTTPException(
            status_code=400,
            detail="Invalid operation"
        )

    return CalculatorResponse(result=result)