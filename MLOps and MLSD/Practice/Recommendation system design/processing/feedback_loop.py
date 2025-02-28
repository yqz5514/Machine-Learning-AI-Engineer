import pandas as pd
import lightgbm as lgb
import joblib

# Load user feedback from interactions
df = pd.read_csv("data/raw/user_interactions.csv")

# Process new user feedback features
df["engagement_score"] = df["watch_time"] + (df["liked"] * 10) + (df["shared"] * 5) - (df["skipped"] * 5)
df_grouped = df.groupby("user_id").agg({
    "engagement_score": "sum",
    "video_id": "count"
}).rename(columns={"video_id": "total_videos_watched"})

df_grouped["avg_engagement_score"] = df_grouped["engagement_score"] / df_grouped["total_videos_watched"]

# Prepare training data
X_train = df_grouped[["total_videos_watched", "avg_engagement_score"]]
y_train = (df_grouped["avg_engagement_score"] > 5).astype(int)  # Simulated engagement threshold

# Load existing ranking model
ranking_model_path = "models/model_registry/ranking_model.pkl"
ranking_model = joblib.load(ranking_model_path)

# Retrain the model with new user feedback
ranking_model.fit(X_train, y_train)

# Save the updated ranking model
joblib.dump(ranking_model, ranking_model_path)
print("✅ Ranking model retrained and updated.")
