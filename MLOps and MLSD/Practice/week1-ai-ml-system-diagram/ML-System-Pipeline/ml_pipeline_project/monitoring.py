from prometheus_client import start_http_server, Summary
import random
import time

# ✅ Uses Prometheus for tracking inference speed
# ✅ Logs time taken per request

request_time = Summary('ml_inference_processing_time', 'Time spent processing ML requests')

@request_time.time()
def process_request():
    time.sleep(random.uniform(0.1, 0.5))

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_request()
