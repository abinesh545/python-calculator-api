from fastapi import FastAPI, HTTPException
from app.calculator import add, subtract, multiply, divide

app = FastAPI()


@app.get("/add")
def add_api(a: float, b: float):
    return {"result": add(a, b)}


@app.get("/subtract")
def subtract_api(a: float, b: float):
    return {"result": subtract(a, b)}


@app.get("/multiply")
def multiply_api(a: float, b: float):
    return {"result": multiply(a, b)}


@app.get("/divide")
def divide_api(a: float, b: float):
    try:
        return {"result": divide(a, b)}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
