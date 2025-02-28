CREATE TABLE IF NOT EXISTS user_interactions (
    user_id INTEGER NOT NULL,
    video_id INTEGER NOT NULL,
    watch_time INTEGER NOT NULL,
    liked BOOLEAN NOT NULL,
    shared BOOLEAN NOT NULL,
    skipped BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY (user_id, video_id, timestamp)
);

CREATE TABLE IF NOT EXISTS video_metadata (
    video_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    duration INTEGER NOT NULL,
    tags TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS model_performance (
    model_name TEXT PRIMARY KEY,
    accuracy FLOAT NOT NULL,
    precision FLOAT NOT NULL,
    recall FLOAT NOT NULL,
    f1_score FLOAT NOT NULL,
    last_updated TIMESTAMP DEFAULT NOW()
);
