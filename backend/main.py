from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import numpy as np
import uvicorn
import pandas as pd
from io import StringIO

from model_api import pipeline_predict, pipeline_fit

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


@app.post("/api/recibir_csv")
async def recibir_csv(file: UploadFile = File(...), model_id: int = Form(...)):
    df = pd.read_csv(file.file)
    df = pipeline_predict(df, model_id)

    output = StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="result.csv"'
    }

    return StreamingResponse(output, media_type='text/csv', headers=headers)


@app.post("/predict")
def predict_body(features: dict):
    if features["koi_prad"] < 20:
        return {"prediction": "Exoplanet"}
    else:
        return {"prediction": "Stellar Companion"}

app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
