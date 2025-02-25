
# ✅ Loads dataset
# ✅ Trains ML model
# ✅ Logs results in MLflow
# ✅ Saves model locally

import os
import joblib
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import logging
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from utils import load_config, setup_logging, load_data

# Setup logging
logger = setup_logging("logs/train.log")

# Load Configuration
config = load_config()
dataset_path = config["dataset"]["path"]
test_size = config["training"]["test_size"]
random_state = config["training"]["random_state"]
param_search = config["model"]["hyperparameters"]["search"]
param_grid = config["model"]["hyperparameters"]["param_grid"]

# Start Logging
logger.info("🔄 Starting ML Model Training Pipeline...")

# Load Dataset
logger.info("📂 Loading dataset...")
try:
    df = load_data(dataset_path)
    X, y = df.iloc[:, :-1], df.iloc[:, -1]
    logger.info(f"✅ Dataset loaded successfully! Shape: {df.shape}")
except Exception as e:
    logger.error(f"❌ Failed to load dataset: {str(e)}")
    exit()

# Feature Scaling
logger.info("🔄 Applying StandardScaler...")
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Splitting Data
logger.info(f"📊 Splitting dataset: {100 * (1 - test_size)}% train, {100 * test_size}% test")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state
)

# MLflow Experiment Tracking
mlflow.set_experiment("ML Model Training")
with mlflow.start_run():
    if param_search:
        logger.info("🔍 Performing Hyperparameter Search (GridSearchCV)...")
        base_model = RandomForestClassifier(random_state=random_state)
        grid_search = GridSearchCV(base_model, param_grid, cv=3, scoring="accuracy", n_jobs=-1)
        grid_search.fit(X_train, y_train)
        best_params = grid_search.best_params_
        model = grid_search.best_estimator_
        logger.info(f"✅ Best Hyperparameters Found: {best_params}")
    else:
        best_params = {
            "n_estimators": config["model"]["hyperparameters"]["param_grid"]["n_estimators"][0],
            "max_depth": config["model"]["hyperparameters"]["param_grid"]["max_depth"][0],
            "criterion": config["model"]["hyperparameters"]["param_grid"]["criterion"][0]
        }
        logger.info(f"🚀 Training RandomForestClassifier with fixed params: {best_params}...")
        model = RandomForestClassifier(**best_params, random_state=random_state)
        model.fit(X_train, y_train)

    # Evaluate Model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)

    # Log Parameters & Metrics
    mlflow.log_params(best_params)
    mlflow.log_metric("accuracy", accuracy)

    # Save Model & Scaler
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    joblib.dump(scaler, "model/scaler.pkl")
    logger.info("💾 Model and scaler saved successfully!")

    # Log Metrics
    logger.info(f"✅ Model Training Complete! Accuracy: {accuracy:.4f}")
    logger.info(f"📊 Classification Report:\n{classification_rep}")

# End Logging
logger.info("🎯 Training pipeline completed successfully!")


# import os
# import joblib
# import pandas as pd
# import numpy as np
# import mlflow
# import mlflow.sklearn
# import logging
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score, classification_report
# from utils import load_config, setup_logging, load_data

# # Setup logging
# logger = setup_logging("logs/train.log")

# # Load Configuration
# config = load_config()
# dataset_path = config["dataset"]["path"]
# test_size = config["training"]["test_size"]
# random_state = config["training"]["random_state"]
# n_estimators = config["model"]["hyperparameters"]["n_estimators"]
# max_depth = config["model"]["hyperparameters"]["max_depth"]

# # Start Logging
# logger.info("🔄 Starting ML Model Training Pipeline...")

# # Load Dataset
# logger.info("📂 Loading dataset...")
# try:
#     df = load_data(dataset_path)
#     X, y = df.iloc[:, :-1], df.iloc[:, -1]
#     logger.info(f"✅ Dataset loaded successfully! Shape: {df.shape}")
# except Exception as e:
#     logger.error(f"❌ Failed to load dataset: {str(e)}")
#     exit()

# # Feature Scaling
# logger.info("🔄 Applying StandardScaler...")
# scaler = StandardScaler()
# X = scaler.fit_transform(X)

# # Splitting Data
# logger.info(f"📊 Splitting dataset: {100 * (1 - test_size)}% train, {100 * test_size}% test")
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=test_size, random_state=random_state
# )

# # MLflow Experiment Tracking
# mlflow.set_experiment("ML Model Training")
# with mlflow.start_run():
#     # Train Model
#     logger.info(f"🚀 Training RandomForestClassifier (n_estimators={n_estimators}, max_depth={max_depth})...")
#     model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
#     model.fit(X_train, y_train)

#     # Evaluate Model
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     classification_rep = classification_report(y_test, y_pred)

#     # Log Parameters & Metrics
#     mlflow.log_param("n_estimators", n_estimators)
#     mlflow.log_param("max_depth", max_depth)
#     mlflow.log_metric("accuracy", accuracy)

#     # Save Model & Scaler
#     os.makedirs("model", exist_ok=True)
#     joblib.dump(model, "model/model.pkl")
#     joblib.dump(scaler, "model/scaler.pkl")
#     logger.info("💾 Model and scaler saved successfully!")

#     # Log Metrics
#     logger.info(f"✅ Model Training Complete! Accuracy: {accuracy:.4f}")
#     logger.info(f"📊 Classification Report:\n{classification_rep}")

# # End Logging
# logger.info("🎯 Training pipeline completed successfully!")
