from fastapi import APIRouter
from funciones.funciones import predict, predict2, Body
router = APIRouter()

@router.post("/predict")
def prediccion(age:int, salary:int):
    return predict(age, salary)

@router.post("/predict2")
def prediccion2(body: Body):
    return predict2(body)