from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import numpy as np
import uvicorn

app = FastAPI()

class Star(BaseModel):
    radius: float
    mass: float
    temperature: float

class Body(BaseModel):
    radius: float

class TransitParams(BaseModel):
    star: Star
    body: Body
    time_scaling_factor: float
    drag_duration: float
    impact_param: float

@app.post("/predict")
def predict_body(features: dict):
    if features["koi_prad"] < 20:
        return {"prediction": "Exoplanet"}
    else:
        return {"prediction": "Stellar Companion"}

app.mount("/", StaticFiles(directory="./frontend/", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
