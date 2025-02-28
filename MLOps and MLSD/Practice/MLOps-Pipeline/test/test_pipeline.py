import pytest
import joblib
import numpy as np
from utils import load_data
from train import train_model
from inference import predict
from fastapi.testclient import TestClient
from serve import app

# Load Model & Scaler
model_path = "model/model.pkl"
scaler_path = "model/scaler.pkl"

@pytest.fixture

def load_trained_model():
    """Ensure the trained model is available before testing."""
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except FileNotFoundError:
        pytest.fail("Model or Scaler file not found. Run `python train.py` first.")

# Ensures dataset loads properly, isn't empty, and has no missing values.
def test_data_loading():
    """Test if dataset loads properly."""
    df = load_data("data/iris.csv")
    assert df.shape[0] > 0  # Ensure the dataset is not empty
    assert df.isnull().sum().sum() == 0  # Ensure no missing values

# Ensures the model and scaler are correctly trained and saved.
def test_model_training():
    """Test if the model trains and saves properly."""
    train_model()  # Train and save the model
    assert joblib.load(model_path) is not None  # Check if model is saved
    assert joblib.load(scaler_path) is not None  # Check if scaler is saved

# Ensures the trained model makes predictions and returns a valid class (0, 1, or 2).
def test_model_inference(load_trained_model):
    """Test if the model makes predictions correctly."""
    model, scaler = load_trained_model
    sample_input = np.array([5.1, 3.5, 1.4, 0.2])
    scaled_input = scaler.transform([sample_input])
    prediction = model.predict(scaled_input)
    assert prediction in [0, 1, 2]  # Ensure valid class prediction

# Sends a request to the FastAPI endpoint and checks if it returns a valid prediction.
def test_api():
    """Test FastAPI endpoint."""
    client = TestClient(app)
    response = client.post("/predict/", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in [0, 1, 2]  # Ensure valid class prediction
