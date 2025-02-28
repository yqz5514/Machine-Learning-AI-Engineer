```
📂 Kafka Architecture
│
├── 1️⃣ **Producers** 📝 (Send Data)
│   ├── Send messages (events) to Kafka topics.
│   ├── Example: User interactions (likes, watch time).
│
├── 2️⃣ **Topics** 📦 (Store Data)
│   ├── Message categories (e.g., "user_interactions").
│   ├── Messages are split into partitions.
│
├── 3️⃣ **Brokers** 🔄 (Manage Kafka Clusters)
│   ├── Store and distribute topic messages.
│   ├── Handle message replication for fault tolerance.
│
├── 4️⃣ **Consumers** 👥 (Read Data)
│   ├── Applications that process real-time data.
│   ├── Example: Updating Redis with new recommendations.
│
└── 5️⃣ **Zookeeper** 🐵 (Manages Kafka)
    ├── Tracks cluster state, leader election.

📂 Kafka in Recommendation System
│
├── 1️⃣ **User Watches a Video → Kafka Producer Sends Event** 📤
│   ├── (ingestion/kafka_producer.py)
│   ├── Event Example: {"user_id": 123, "video_id": 45, "watch_time": 120}
│
├── 2️⃣ **Kafka Stores the Event in a Topic** 📦
│   ├── Topic: "user_interactions"
│   ├── Broker stores and partitions messages.
│
├── 3️⃣ **Kafka Consumer Reads the Event → Updates Database** 👥
│   ├── (processing/stream_processing.py)
│   ├── Updates PostgreSQL and Redis with new recommendations.
│
└── 4️⃣ **API Fetches Fresh Recommendations from Redis** 🚀
    ├── (serving/serve.py)
    ├── FastAPI serves recommendations instantly.
```
### 📌 Why Use Kafka Instead of Traditional Methods?
- Feature	Kafka ✅	Batch Processing ❌
- Real-time event handling	✅ Yes	❌ No
- Handles high data volume	✅ Yes (millions of events/sec)	❌ No (slow)
- Scales horizontally	✅ Yes	❌ No
- Ensures data integrity	✅ Yes	❌ No (loses events if failed)
- Reduces API latency	✅ Yes (preprocessed recommendations)	❌ No (delayed updates)


