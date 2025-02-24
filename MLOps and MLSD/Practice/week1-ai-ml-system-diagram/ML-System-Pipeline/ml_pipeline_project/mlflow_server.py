# This script starts the MLflow tracking server to monitor model versions.
import os

os.system("mlflow server --host 0.0.0.0 --port 5001")

# Allows you to track experiments in a web UI.
# Helps compare different model training runs.