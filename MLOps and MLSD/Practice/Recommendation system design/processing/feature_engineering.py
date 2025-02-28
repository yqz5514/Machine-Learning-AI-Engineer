import pandas as pd
import numpy as np
# Creates computed User & Video features for better model input.

# Load raw user interactions
df = pd.read_csv("data/raw/user_interactions.csv")

# Generate features
df["interaction_score"] = df["watch_time"] + (df["liked"] * 10) + (df["shared"] * 5) - (df["skipped"] * 5)
df["normalized_watch_time"] = df["watch_time"] / df["watch_time"].max()

# Save processed features
df.to_csv("data/processed/user_profiles.csv", index=False)
print("✅ Feature engineering complete and saved.")
