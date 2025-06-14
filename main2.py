from pydantic import BaseModel
from fastapi import FastAPI

import joblib


app = FastAPI()

class Body(BaseModel):
    age: int
    salary: int

@app.get("/")
def saludo():
    return {"message": "Hola mundo"}


@app.post("/predict")
def predict(age: int, salary: int) -> dict:
    model = joblib.load("arbol.pkl")
    prediction = model.predict([[age, salary]])
    msg = ""
    if prediction[0] == 0:
        msg = "No comprara!"
    else:
        msg = "Comprara!"
    return { "message": msg }


@app.post("/predict2")
def predict2(body: Body) -> dict:
    model = joblib.load("arbol.pkl")
    prediction = model.predict([[body.age, body.salary]])
    msg = ""
    if prediction[0] == 0:
        msg = "No comprara!"
    else:
        msg = "Comprara!"