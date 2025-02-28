# 📌 Designing Machine Learning Systems - Chapter 3.4 Summary: Modes of Dataflow

## **📌 Understanding Dataflow in ML Systems**
In production ML systems, **data needs to flow between multiple processes**.  
Since different processes **do not share memory**, data must be transferred using structured mechanisms.

### **Three Modes of Dataflow**:
1. **Data passing through databases**
2. **Data passing through services (e.g., REST, RPC APIs)**
3. **Data passing through real-time transport (e.g., Apache Kafka, Amazon Kinesis)**

📌 **Key Takeaway**: **Choosing the right mode of data transfer depends on latency, scalability, and application constraints.**

---

## **📌 1. Data Passing Through Databases**
- The simplest way to transfer data **between processes** is via **a shared database**.
- **Process A writes data → Process B reads data**.

### **🚨 Limitations**
1. **Both processes must access the same database** → **Not feasible** for cross-company services.
2. **Database reads/writes can be slow** → **Not ideal for real-time applications**.

📌 **Best For**: **Batch processing, data warehousing, non-time-sensitive applications**.

---

## **📌 2. Data Passing Through Services**
- **Processes communicate via direct network requests** (e.g., REST APIs, RPC calls).
- A service is **a process that is accessible remotely**.

### **📌 Microservice Architecture**
- Structuring an application as independent **services** enables **scalability and modular development**.
- Example: **Ride-sharing app (e.g., Lyft, Uber)**

| **Service** | **Function** |
|------------|-------------|
| **Driver Management Service** | Predicts how many drivers are available. |
| **Ride Management Service** | Predicts how many rides are requested. |
| **Price Optimization Service** | Determines optimal ride pricing based on supply & demand. |

### **🚀 REST vs. RPC**
| **Feature** | **REST (Representational State Transfer)** | **RPC (Remote Procedure Call)** |
|------------|--------------------------------|---------------------------|
| **Design** | Built for network-based requests. | Makes remote calls look like local function calls. |
| **Best Use Case** | **Public APIs, web-based services**. | **Internal services within an organization**. |

📌 **Best For**: **Service-based architectures, cross-application communication**.

---

## **📌 3. Data Passing Through Real-Time Transport**
- A **real-time event-driven architecture** coordinates data flow between services **asynchronously**.
- Instead of direct service-to-service requests, services **publish data to a broker**, and other services **subscribe** to the data.

### **🚀 Why Use Real-Time Transports?**
1. **Scalability** → No direct service dependencies.
2. **Resiliency** → A service failure does not break the entire system.
3. **Low-latency streaming** → Optimized for real-time ML applications.

### **📌 PubSub vs. Message Queues**
| **Mode** | **Description** | **Examples** |
|---------|---------------|------------|
| **PubSub (Publish-Subscribe)** | Any service can **publish** events, and any subscriber can **consume** them. | **Apache Kafka, Amazon Kinesis** |
| **Message Queues** | Messages are sent **to specific consumers**. | **RabbitMQ, Apache RocketMQ** |

📌 **Best For**: **Real-time ML pipelines, event-driven architectures, streaming analytics**.

---

## **📌 4. Batch Processing vs. Stream Processing**
Once data reaches **storage (databases, lakes, warehouses)**, it can be processed **historically or in real-time**.

| **Processing Type** | **Definition** | **Example Use Case** | **Tools** |
|-------------------|---------------|------------------|----------|
| **Batch Processing** | **Scheduled periodic jobs** process historical data. | Compute **daily average surge pricing** for rides. | **Apache Spark, MapReduce** |
| **Stream Processing** | **Continuous real-time computation** on streaming data. | Adjust pricing **dynamically based on live demand**. | **Apache Flink, KSQL, Spark Streaming** |

📌 **Key Takeaway**: **Batch processing generates "static" features, while stream processing generates "dynamic" features**.

---

## **📌 Chapter 3 Summary: The Role of Data in ML Systems**
### **1️⃣ Choosing the Right Data Format**
- **Row-major vs. Column-major**
- **Text vs. Binary Formats**

📌 **Key Takeaway**: **The right data format optimizes storage and retrieval for specific ML applications.**

---

### **2️⃣ Data Models for ML Systems**
| **Model** | **Description** | **Best For** |
|---------|---------------|------------|
| **Relational Model (SQL)** | Structured, normalized data with relations. | **OLTP systems, structured analytics**. |
| **Document Model (NoSQL, JSON, BSON)** | Semi-structured data, self-contained documents. | **Content management, flexible data storage**. |
| **Graph Model (Nodes & Edges)** | Optimized for relationships and connections. | **Social networks, recommendation systems**. |

📌 **Key Takeaway**: **Different data models serve different ML system needs.**

---

### **3️⃣ Data Storage Engines & Processing**
| **Database Type** | **Optimized For** | **Examples** |
|---------------|--------------|------------|
| **Transactional DBs (OLTP)** | **Real-time transactions** | PostgreSQL, MySQL, CockroachDB |
| **Analytical DBs (OLAP)** | **Complex aggregations & ML workloads** | Snowflake, BigQuery, Apache Iceberg |

📌 **Key Takeaway**: **OLTP and OLAP databases are increasingly being merged for hybrid data workloads.**

---

### **4️⃣ Dataflow Modes in ML Systems**
| **Mode** | **Best For** |
|---------|-------------|
| **Databases** | Simple **data passing**, batch processing. |
| **Services (APIs)** | Microservices, REST/RPC-based interactions. |
| **Real-time Transport (Event-driven)** | Scalable, asynchronous ML data pipelines. |

📌 **Key Takeaway**: **The right dataflow mechanism improves efficiency and scalability in ML pipelines.**

---

## **📌 Key Interview Questions & Answers**
### **❓ Q1: How do batch processing and stream processing differ in ML systems?**
✅ **Answer:**  
- **Batch processing** runs at fixed intervals and is used for **static ML features** (e.g., daily sales aggregation).  
- **Stream processing** continuously updates data for **real-time ML inference** (e.g., dynamic ride pricing in Lyft).  

📌 **Example**: Batch processing computes **average ride prices over a week**, while stream processing **adjusts ride prices in real-time**.

---

### **❓ Q2: Why is a real-time transport system (e.g., Kafka, Kinesis) preferred over direct service-to-service communication in ML applications?**
✅ **Answer:**  
- **Decouples services** → No direct dependencies between ML components.  
- **Asynchronous processing** → Enables **low-latency AI decision-making**.  
- **Fault tolerance** → One service failure **doesn’t crash the entire system**.  

📌 **Example**: A fraud detection ML system can **publish live fraud signals** that multiple downstream AI applications consume.

---

### **❓ Q3: What are the trade-offs between using REST APIs vs. real-time messaging for data transfer?**
✅ **Answer:**  
| **Method** | **Pros** | **Cons** |
|----------|--------|--------|
| **REST APIs** | ✅ Simple, widely used ✅ Stateless | ❌ High latency ❌ Requires synchronous communication |
| **Real-time Messaging (Kafka, RabbitMQ)** | ✅ Low latency ✅ Supports asynchronous processing | ❌ More complex setup ❌ Requires monitoring |

📌 **Example**: **REST APIs work well for traditional web services**, while **real-time messaging is better for event-driven ML pipelines**.

---

## **📌 Final Takeaways (3-Sentence Summary)**
1️⃣ **ML systems must handle various data formats, models, and storage engines for efficient processing.**  
2️⃣ **Dataflow can be managed via databases, services, or real-time transport, depending on system needs.**  
3️⃣ **Stream processing is increasingly crucial for real-time AI applications, offering scalable, event-driven architectures.**  

---
