import joblib
from pydantic import BaseModel

class Body(BaseModel):
    age: int
    salary: int


def predict(age: int, salary: int) -> dict:
    model = joblib.load("arbol.pkl")
    prediction = model.predict([[age, salary]])
    msg = ""
    if prediction[0] == 0:
        msg = "No comprara!"
    else:
        msg = "Comprara!"
    return { "message": msg }



def predict2(body: Body) -> dict:
    model = joblib.load("arbol.pkl")
    prediction = model.predict([[body.age, body.salary]])
    msg = ""
    if prediction[0] == 0:
        msg = "No comprara!"
    else:
        msg = "Comprara!"
    return { "message": msg }