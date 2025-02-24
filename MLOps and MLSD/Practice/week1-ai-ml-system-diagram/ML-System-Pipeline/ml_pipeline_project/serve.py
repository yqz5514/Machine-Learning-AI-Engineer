from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

#Model Inference API
# ✅ Loads the trained model
# ✅ Accepts JSON requests for predictions
# ✅ Uses FastAPI for faster performance

app = FastAPI()
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

class ModelInput(BaseModel):
    features: list

@app.post("/predict/")
async def predict(data: ModelInput):
    scaled_data = scaler.transform([data.features])
    prediction = model.predict(scaled_data)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
