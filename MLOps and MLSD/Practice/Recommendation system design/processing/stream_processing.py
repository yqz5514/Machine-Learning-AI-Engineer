import json
from kafka import KafkaConsumer
import psycopg2
import redis

# Reads real-time Kafka messages and updates PostgreSQL & Redis.

# PostgreSQL Connection Settings
DB_NAME = "recommendation_db"
DB_USER = "postgres"
DB_PASSWORD = "yourpassword"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cursor = conn.cursor()

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Kafka Consumer
consumer = KafkaConsumer(
    "user_interactions",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    event = message.value
    print(f"Consumed: {event}")

    # Store event in PostgreSQL
    cursor.execute(
        "INSERT INTO user_interactions (user_id, video_id, watch_time, liked, shared, skipped, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (event["user_id"], event["video_id"], event["watch_time"], bool(event["liked"]), bool(event["shared"]), bool(event["skipped"]), event["timestamp"])
    )

    # Update Redis Cache with Fresh Recommendations
    new_recommendations = [event["video_id"]]  # Simulate recommendation update
    redis_client.setex(f"user:{event['user_id']}:recommendations", 3600, json.dumps(new_recommendations))

    conn.commit()
