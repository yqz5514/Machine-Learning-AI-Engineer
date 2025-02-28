import psycopg2
import pandas as pd

# Database connection settings (Modify with actual credentials)
DB_NAME = "recommendation_db"
DB_USER = "postgres"
DB_PASSWORD = "yourpassword"
DB_HOST = "localhost"  # Change to your PostgreSQL host
DB_PORT = "5432"

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

# Create user interactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_interactions (
    user_id INTEGER,
    video_id INTEGER,
    watch_time INTEGER,
    liked BOOLEAN,
    shared BOOLEAN,
    skipped BOOLEAN,
    timestamp TIMESTAMP
)
''')

# Load CSV data into DataFrame
df = pd.read_csv("data/raw/user_interactions.csv")

# Insert data into PostgreSQL
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO user_interactions (user_id, video_id, watch_time, liked, shared, skipped, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (row["user_id"], row["video_id"], row["watch_time"], bool(row["liked"]), bool(row["shared"]), bool(row["skipped"]), row["timestamp"])
    )

conn.commit()
cursor.close()
conn.close()
print("✅ User interactions data successfully ingested into PostgreSQL.")
