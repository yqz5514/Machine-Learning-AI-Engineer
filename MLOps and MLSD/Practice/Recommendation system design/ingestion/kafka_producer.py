import json
from kafka import KafkaProducer
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

users = list(range(1, 1000))
videos = list(range(1, 100))

while True:
    event = {
        "user_id": random.choice(users),
        "video_id": random.choice(videos),
        "watch_time": random.randint(1, 300),
        "liked": random.choice([0, 1]),
        "shared": random.choice([0, 1]),
        "skipped": random.choice([0, 1]),
        "timestamp": time.time()
    }
    producer.send("user_interactions", value=event)
    print(f"Produced: {event}")
    time.sleep(1)  # Simulate real-time events
