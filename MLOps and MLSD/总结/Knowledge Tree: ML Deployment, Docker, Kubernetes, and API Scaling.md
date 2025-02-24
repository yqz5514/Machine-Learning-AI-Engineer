```text
📂 Machine Learning Deployment
│
├── 🚀 Why Deploy an ML Model?
│   ├── 🔹 Make ML models accessible to users and applications.
│   ├── 🔹 Automate model inference (no need to run manually).
│   ├── 🔹 Enable real-time predictions via API.
│   ├── 🔹 Scale ML models to handle high traffic.
│
├── 🌍 ML API Deployment
│   ├── 🔹 Converts ML models into **FastAPI or Flask** services.
│   ├── 🔹 Users send JSON requests, API processes them, and returns predictions.
│   ├── 📌 Example:
│   │   ├── **Input:** `{"features": [5.1, 3.5, 1.4, 0.2]}`
│   │   ├── **ML Model Processes Data**
│   │   ├── **Output:** `{"prediction": 0}`
│   ├── 🔹 API Deployment Methods:
│   │   ├── 🖥️ **Local Machine** – Runs API on your laptop (not accessible globally).
│   │   ├── ☁️ **Cloud VM (AWS, GCP, Azure)** – Deploys API on a cloud server.
│   │   ├── 📦 **Docker Container** – Packages API with dependencies for easy deployment.
│   │   ├── ⚡ **Serverless (AWS Lambda, Google Cloud Functions)** – API runs **only when needed**.
│
├── 📦 What is Docker?
│   ├── 🔹 A containerization tool that **packages applications + dependencies**.
│   ├── 🔹 Ensures the model runs **identically** on any machine.
│   ├── 📌 Key Components:
│   │   ├── **Docker Image** – A blueprint of the application (like a frozen pizza 🍕).
│   │   ├── **Docker Container** – A running instance of the image (a cooked pizza 🍕).
│   │   ├── **Dockerfile** – A script defining how to build the image.
│   ├── 📌 Example:
│   │   ├── `docker build -t ml-api .` → **Creates Docker Image**
│   │   ├── `docker run -p 5000:5000 ml-api` → **Runs API inside a container**
│
├── ☸️ What is Kubernetes?
│   ├── 🔹 A tool for **orchestrating multiple Docker containers**.
│   ├── 🔹 Manages **scalability, load balancing, and fault tolerance**.
│   ├── 📌 Key Components:
│   │   ├── **Pods** – Smallest deployable unit (runs a single or multiple containers).
│   │   ├── **Deployments** – Ensures the right number of containers are running.
│   │   ├── **Services** – Makes containers accessible via a network.
│   │   ├── **Horizontal Pod Autoscaler (HPA)** – Scales containers when CPU usage is high.
│
├── 🔄 Why Scale ML APIs?
│   ├── 🔹 Prevents **API slowdowns or crashes** when too many users send requests.
│   ├── 🔹 Distributes workload **across multiple containers**.
│   ├── 🔹 Ensures **high availability** (system keeps running even if one container fails).
│
├── 📈 Auto-Scaling ML API with Kubernetes
│   ├── 🔹 Uses **Horizontal Pod Autoscaler (HPA)** to dynamically scale up/down containers.
│   ├── 🔹 🚀 Example of Scaling:
│   │   ├── **1:00 PM** – 50 requests/sec → **1 container handles it fine**.
│   │   ├── **1:10 PM** – 200 requests/sec → **Kubernetes adds 2 more containers**.
│   │   ├── **1:20 PM** – 500 requests/sec → **Scales to 5 containers to avoid crashes**.
│   ├── 📌 Kubernetes Scaling Commands:
│   │   ├── `kubectl apply -f k8s-deployment.yaml` → Deploys ML API.
│   │   ├── `kubectl apply -f hpa.yaml` → Enables auto-scaling.
│   │   ├── `kubectl get pods` → Checks how many containers are running.
│
└── 🔥 Summary of Key Concepts
    ├── **ML Deployment:** Make models available via APIs.
    ├── **Docker:** Packages ML models into portable containers.
    ├── **Kubernetes:** Manages and scales ML containers efficiently.
    ├── **Scaling:** Prevents slow response times when traffic increases.
    ├── **Kubernetes Autoscaler:** Adds/removes containers based on demand.

```