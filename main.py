from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

cars_db = []

class Characteristic(BaseModel):
    max_speed: float = Field(..., gt=0, description="Vitesse maximale en km/h")
    max_fuel_capacity: float = Field(..., gt=0, description="Capacité maximale du réservoir en litres")

@app.get("/ping")
def ping():
    return {"message": "pong"}





    