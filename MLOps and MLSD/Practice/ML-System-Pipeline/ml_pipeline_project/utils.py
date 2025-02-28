# This script contains helper functions for logging, data loading, and configuration handling.
# Reusability – Keeps logging, config loading, and dataset handling modular.
# Error handling – Prevents dataset and logging failures.
import yaml
import logging
import pandas as pd
import os

def load_config(config_path="config.yaml"):
    """Load YAML configuration file."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def setup_logging(log_file="logs/training.log"):
    """Configure logging settings."""
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger(__name__)

def load_data(file_path):
    """Load dataset from CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found: {file_path}")
    df = pd.read_csv(file_path)
    return df
