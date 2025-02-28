import pandas as pd

df = pd.read_csv("data/raw/user_interactions.csv")
df.to_parquet("storage/user_interactions.parquet")
print("Data saved to Parquet format for Data Lakehouse.")
