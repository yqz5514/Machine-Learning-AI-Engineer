# load the trained model and test predictions manually
# Tests model predictions before deploying the API.
# Helps debug errors before FastAPI serving.

import joblib
import numpy as np
from utils import setup_logging

logger = setup_logging()

# Load Model & Scaler
try:
    model = joblib.load("model/model.pkl")
    scaler = joblib.load("model/scaler.pkl")
    logger.info("Model and Scaler loaded successfully.")
except FileNotFoundError:
    logger.error("Model or Scaler file not found. Run `train.py` first.")
    exit()

def predict(features):
    """Run model inference on input features."""
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)
    return prediction[0]

if __name__ == "__main__":
    sample_input = np.array([5.1, 3.5, 1.4, 0.2])  # Example input
    result = predict(sample_input)
    logger.info(f"Prediction: {result}")
