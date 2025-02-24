# This script evaluates the trained model using accuracy, F1-score, and classification reports.
# Ensures model performance tracking.
# Helps compare different model versions.
from sklearn.metrics import accuracy_score, classification_report
import logging
from utils import setup_logging

logger = setup_logging()

def evaluate_model(model, X_test, y_test):
    """Evaluates the model on test data."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    logger.info(f"Model Accuracy: {accuracy:.4f}")
    logger.info("Classification Report:\n" + report)

    return accuracy, report
