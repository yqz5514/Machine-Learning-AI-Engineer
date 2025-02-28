import psycopg2
import pandas as pd
# Processes batch user features from PostgreSQL and saves them to CSV.
# PostgreSQL Connection Settings
DB_NAME = "recommendation_db"
DB_USER = "postgres"
DB_PASSWORD = "yourpassword"
DB_HOST = "localhost"
DB_PORT = "5432"

def process_user_features():
    """Generate user feature aggregates for batch recommendations."""
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cursor = conn.cursor()
    
    query = """
    SELECT user_id, 
           COUNT(video_id) AS total_videos_watched,
           AVG(watch_time) AS avg_watch_time,
           SUM(liked::int) AS total_likes
    FROM user_interactions
    GROUP BY user_id;
    """
    
    cursor.execute(query)
    user_features = cursor.fetchall()
    
    df = pd.DataFrame(user_features, columns=["user_id", "total_videos_watched", "avg_watch_time", "total_likes"])
    df.to_csv("data/processed/user_profiles.csv", index=False)
    
    cursor.close()
    conn.close()
    print("✅ User features processed and saved.")
