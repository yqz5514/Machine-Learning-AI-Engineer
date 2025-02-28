import pandas as pd
import lightgbm as lgb
import joblib

# Load processed user interaction features
df = pd.read_csv("data/processed/user_profiles.csv")

# Define features & labels for training
X_train = df[["total_videos_watched", "avg_watch_time", "total_likes"]]
y_train = (df["total_likes"] > 5).astype(int)  # Simulated ranking label

# Train ranking model
model = lgb.LGBMClassifier()
model.fit(X_train, y_train)

# Save the trained ranking model for serving
joblib.dump(model, "models/model_registry/ranking_model.pkl")
print("✅ Ranking model trained and saved.")
