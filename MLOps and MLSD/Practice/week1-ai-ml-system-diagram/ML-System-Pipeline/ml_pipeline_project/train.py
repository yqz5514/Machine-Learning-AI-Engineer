import joblib
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from utils import load_config, load_data, setup_logging
from model_evaluation import evaluate_model
# ✅ Loads dataset
# ✅ Trains ML model
# ✅ Logs results in MLflow
# ✅ Saves model locally

# Load Config & Logger
config = load_config()
logger = setup_logging()

# Load Data
df = load_data(config["dataset"]["path"])
X, y = df.iloc[:, :-1], df.iloc[:, -1]

# Feature Scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=config["training"]["test_size"], random_state=config["training"]["random_state"]
)

# MLflow Experiment
mlflow.set_experiment("ML Model Training")
with mlflow.start_run():
    model = RandomForestClassifier(
        n_estimators=config["model"]["hyperparameters"]["n_estimators"],
        max_depth=config["model"]["hyperparameters"]["max_depth"],
        random_state=config["training"]["random_state"]
    )
    model.fit(X_train, y_train)

    # Log Parameters & Metrics
    mlflow.log_param("n_estimators", config["model"]["hyperparameters"]["n_estimators"])
    mlflow.log_param("max_depth", config["model"]["hyperparameters"]["max_depth"])
    
    accuracy, _ = evaluate_model(model, X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    # Save Model to MLflow & Locally
    mlflow.sklearn.log_model(model, "model")
    joblib.dump(model, "model/model.pkl")
    joblib.dump(scaler, "model/scaler.pkl")

logger.info("Training complete. Model saved.")
