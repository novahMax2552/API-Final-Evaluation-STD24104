from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

cars_db = []

class Characteristic(BaseModel):
    max_speed: float = Field(..., gt=0, description="Maximal Speed")
    max_fuel_capacity: float = Field(..., gt=0, description="Maximal Capacity")

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/cars", response_model=List[Car])
def create_cars(cars: List[Car]):
    if not cars:
        raise HTTPException(status_code=400, detail="Error: Car's list cannot be empty")
    cars_db.extend(cars)
    return cars_db

@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars_db




    