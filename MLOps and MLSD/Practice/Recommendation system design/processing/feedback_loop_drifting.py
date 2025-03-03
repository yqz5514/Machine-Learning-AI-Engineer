# Periodically retrain models using new user interactions.
# Update feature embeddings and retrain ranking models every week/month.
# Prevents unnecessary retraining, improving system efficiency.
# Checks for drift before retraining the ranking model.
import pandas as pd
import lightgbm as lgb
import joblib
from monitoring.prometheus_metrics import detect_feature_drift

# Load user feedback from interactions
df = pd.read_csv("data/raw/user_interactions.csv")

# Detect if feature drift occurred
detect_feature_drift()

# Process new user feedback features
df["engagement_score"] = df["watch_time"] + (df["liked"] * 10) + (df["shared"] * 5) - (df["skipped"] * 5)
df_grouped = df.groupby("user_id").agg({
    "engagement_score": "sum",
    "video_id": "count"
}).rename(columns={"video_id": "total_videos_watched"})

df_grouped["avg_engagement_score"] = df_grouped["engagement_score"] / df_grouped["total_videos_watched"]

# Prepare training data
X_train = df_grouped[["total_videos_watched", "avg_engagement_score"]]
y_train = (df_grouped["avg_engagement_score"] > 5).astype(int)

# Load existing ranking model
ranking_model_path = "models/model_registry/ranking_model.pkl"
ranking_model = joblib.load(ranking_model_path)

# Retrain the model only if drift is detected
if detect_feature_drift() > 0.1:  # Threshold for drift
    print("🚨 Data Drift Detected! Retraining Model...")
    ranking_model.fit(X_train, y_train)
    joblib.dump(ranking_model, ranking_model_path)
    print("✅ Model Updated!")
else:
    print("✅ No Significant Drift. Model Not Updated.")
