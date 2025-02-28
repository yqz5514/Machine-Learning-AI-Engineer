import requests
import json

API_URL = "https://api.example.com/videos"

response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    with open("storage/external_videos.json", "w") as f:
        json.dump(data, f)
    print("External video data saved.")
else:
    print("Failed to fetch data from third-party API.")
