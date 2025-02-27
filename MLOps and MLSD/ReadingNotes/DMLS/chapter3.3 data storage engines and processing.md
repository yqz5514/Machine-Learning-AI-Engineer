# 📌 Designing Machine Learning Systems - Chapter 3.3 Summary: Data Storage Engines and Processing

## **📌 What Are Data Storage Engines?**
Data storage engines, also known as **databases**, handle **how data is stored and retrieved**.  
- **Data formats and data models** define **how users interact** with the data.
- **Storage engines** define **how data is physically managed**.

📌 **Key Takeaway**: **Choosing the right storage engine impacts system performance, scalability, and efficiency.**

---

## **📌 1. Transactional vs. Analytical Processing**
Databases are typically **optimized** for two types of workloads:

| **Processing Type** | **Purpose** | **Characteristics** | **Example Use Cases** |
|-------------------|------------|----------------|----------------|
| **OLTP (Online Transaction Processing)** | Handles frequent **real-time transactions**. | ✅ Low latency ✅ High availability ✅ Often **ACID-compliant** ✅ Row-major storage | **Banking**, **E-commerce**, **Ride-sharing apps**, **Social media interactions** |
| **OLAP (Online Analytical Processing)** | Optimized for **complex queries** and **aggregations**. | ✅ Handles large datasets ✅ Columnar storage ✅ High read efficiency | **Business Intelligence**, **Machine Learning Pipelines**, **Data Warehouses** |

📌 **Key Takeaway**: **OLTP ensures fast transaction processing, while OLAP is designed for large-scale data analysis.**

---

## **📌 2. ACID Properties of Transactional Databases**
**Transactional databases (OLTP)** are often designed to **guarantee consistency and reliability** through **ACID properties**:

| **ACID Property** | **Definition** | **Example** |
|------------------|--------------|-----------|
| **Atomicity** | A transaction must be **fully completed or fully rolled back**. | If a **payment fails**, the order **isn’t processed**. |
| **Consistency** | Data must always **follow predefined integrity rules**. | Transactions must involve **valid users** only. |
| **Isolation** | Transactions must execute **as if they were isolated**. | Two users **can’t book the same ride at the same time**. |
| **Durability** | Committed transactions must **persist even after system failure**. | If your phone dies after ordering a ride, your ride still arrives. |

📌 **Key Takeaway**: **ACID ensures that databases remain consistent, even in failure scenarios. However, some developers prefer more flexible systems that sacrifice ACID for performance.**

---

## **📌 3. Merging OLTP & OLAP: The Future of Hybrid Databases**
The distinction between **OLTP and OLAP** is **blurring**:
- **Transactional databases (e.g., CockroachDB)** now support analytical queries.
- **Analytical databases (e.g., Apache Iceberg, DuckDB)** can handle transactional workloads.
- **Storage and compute are decoupled** to improve scalability (**e.g., BigQuery, Snowflake, IBM, Teradata**).

📌 **Key Takeaway**: **Modern data architectures increasingly blend OLTP and OLAP functionalities for efficiency and flexibility.**

---

## **📌 4. Online vs. Nearline vs. Offline Processing**
The term **"online"** in data processing can mean different things:

| **Processing Type** | **Definition** | **Example** |
|-------------------|--------------|-----------|
| **Online Processing** | Data is **immediately available** for input/output. | **Real-time recommendation systems**. |
| **Nearline Processing** | Data is **not immediately available** but can be **quickly retrieved**. | **Cached analytics dashboards**. |
| **Offline Processing** | Data requires **manual intervention** to be used. | **Batch data processing for AI training**. |

📌 **Key Takeaway**: **Choosing between online, nearline, and offline processing depends on speed, cost, and application requirements.**

---

## **📌 5. ETL vs. ELT: Data Transformation Pipelines**
To ensure structured, usable data, **ETL (Extract, Transform, Load)** and **ELT (Extract, Load, Transform)** pipelines are widely used.

### **1️⃣ ETL (Extract, Transform, Load)**
1. **Extract** → Retrieve data from multiple sources.
2. **Transform** → Clean, join, and preprocess data.
3. **Load** → Store the processed data in a database or data warehouse.

📌 **Example**:  
- Convert **gender labels ("Male", "Female")** from different sources into a **standardized format ("M", "F")**.
- Aggregate sales data from **multiple stores** into a **central database**.

### **2️⃣ ELT (Extract, Load, Transform)**
- Instead of **transforming before storage**, raw data is **first loaded into storage** and then processed.
- **Pros**:
  - Faster **data ingestion**.
  - Allows **schema flexibility** (e.g., Data Lakes).
- **Cons**:
  - Querying raw data **is inefficient at scale**.
  - Requires **more compute resources**.

📌 **Key Takeaway**:  
- **ETL** is better for **structured data and predefined schemas**.  
- **ELT** is useful when **raw data needs to be stored first and processed later**.  

---

## **📌 6. Evolution of Data Storage: From Data Lakes to Data Lakehouses**
### **1️⃣ Data Lakes**
- Store **raw, unstructured data**.
- **Pros**: Flexible, schema-free.
- **Cons**: Harder to query efficiently.

### **2️⃣ Data Warehouses**
- Store **structured, preprocessed data**.
- **Pros**: Optimized for analytics, faster queries.
- **Cons**: Rigid schema, preprocessing required.

### **3️⃣ Hybrid Approach: Data Lakehouses**
- **Combine the best of both worlds**:
  - **Flexibility of Data Lakes**.
  - **Performance of Data Warehouses**.
- **Examples**: **Databricks, Snowflake**.

📌 **Key Takeaway**: **Lakehouses allow for fast queries while maintaining flexibility.**

---

## **📌 Key Interview Questions & Answers**
### **❓ Q1: What are the differences between OLTP and OLAP databases?**
✅ **Answer:**  
- **OLTP** (Online Transaction Processing) → Handles **real-time transactions** (e.g., banking, e-commerce).  
- **OLAP** (Online Analytical Processing) → Optimized for **complex queries & aggregations** (e.g., business intelligence).  
- **Key Difference**: OLTP uses **row-major storage**, while OLAP uses **columnar storage** for faster analytics.  

📌 **Example**: A **ride-sharing app** needs OLTP for **real-time ride bookings** but OLAP for **analyzing demand patterns**.

---

### **❓ Q2: How do ETL and ELT differ in data processing?**
✅ **Answer:**  
| **Method** | **Transformation Stage** | **Best For** |
|-----------|------------------|------------|
| **ETL (Extract, Transform, Load)** | Data is transformed **before storage**. | Structured data with **predefined schemas**. |
| **ELT (Extract, Load, Transform)** | Data is stored **before transformation**. | **Raw data lakes** needing flexible processing. |

📌 **Example**:  
- **ETL** → A financial institution preprocesses transactions **before storing them in a data warehouse**.  
- **ELT** → A social media company **stores all user-generated content first** before processing trends.  

---

### **❓ Q3: Why are data lakehouses gaining popularity over data lakes and data warehouses?**
✅ **Answer:**  
- **Data lakes** are flexible but **inefficient for querying**.  
- **Data warehouses** allow fast queries but **require rigid schemas**.  
- **Data lakehouses** combine both:  
  ✅ **Schema flexibility** (like Data Lakes).  
  ✅ **Query efficiency** (like Data Warehouses).  

📌 **Example**: **Snowflake & Databricks** offer **lakehouse solutions** to balance **storage flexibility & performance**.

---

## **📌 Key Takeaways (3-Sentence Summary)**
1️⃣ **Databases are evolving from rigid OLTP/OLAP models to hybrid solutions with decoupled storage & compute.**  
2️⃣ **ETL processes transform data before storage, while ELT prioritizes fast ingestion before processing.**  
3️⃣ **Data lakehouses provide a scalable and efficient alternative, blending the benefits of data lakes and warehouses.**  

---
