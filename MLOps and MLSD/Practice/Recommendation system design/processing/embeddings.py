import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Creates embeddings for videos based on category & duration.



# Load video metadata
df = pd.read_csv("data/raw/videos_metadata.csv")

# Simulate embeddings using normalized duration and category encoding
scaler = StandardScaler()
df["duration_scaled"] = scaler.fit_transform(df[["duration"]])
df["category_encoded"] = df["category"].astype("category").cat.codes

# Create embeddings matrix
embeddings = np.column_stack((df["duration_scaled"], df["category_encoded"]))

# Save embeddings
np.save("data/processed/video_embeddings.npy", embeddings)
print("✅ Video embeddings saved.")
