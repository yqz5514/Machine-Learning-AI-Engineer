# 📌 Designing Machine Learning Systems - Chapter 3.2 Summary: Data Model

## **📌 What is a Data Model?**
A **data model** defines how data is **structured, stored, and retrieved**.

There are three major data models:
1. **Relational Model** (SQL-based)
2. **NoSQL Models** (Document & Graph Models)
3. **Structured vs. Unstructured Data** (Data Warehouses vs. Data Lakes)

📌 **Key Takeaway**: **Choosing the right data model depends on storage efficiency, retrieval speed, and the nature of relationships within the data.**

---

## **📌 1. Relational Model (SQL-Based)**
The **relational model** organizes data into **relations (tables)**, where each relation is a **set of tuples (rows).**

### **Key Characteristics**
- **Relations are unordered** → Row and column order does not matter.
- **Normalization** → Data is often structured using **normal forms (1NF, 2NF, etc.)** to reduce redundancy.
- **Joins can be costly** → Normalized data is split across multiple tables, making queries expensive.
- **Uses SQL (Structured Query Language)** → SQL tables are similar to relational tables but allow **duplicate rows**, which true relations do not.

### **SQL vs. Python Paradigm**
| **Programming Paradigm** | **Description** |
|-------------------------|----------------|
| **Declarative (SQL)** | Specifies **what data is needed**, and the system determines how to fetch it. |
| **Imperative (Python)** | Specifies **step-by-step instructions** to retrieve data. |

### **Query Optimization**
- **Query optimizers** determine the most efficient way to execute a query.
- **ML-based query optimizers** can improve query execution speed by learning from past queries.

📌 **Key Takeaway**: **The relational model is well-suited for structured data with strong consistency requirements but may struggle with large-scale joins.**

---

## **📌 2. NoSQL Models**
**NoSQL** originally meant **"No SQL"** but is now interpreted as **"Not Only SQL"** because many NoSQL databases support relational models.  

There are **two primary NoSQL models**:
1. **Document Model**  
2. **Graph Model**  

---

### **2.1 Document Model (JSON, XML, BSON)**
A **document database** stores **self-contained documents**, often encoded as:
- **JSON** (JavaScript Object Notation)
- **XML** (Extensible Markup Language)
- **BSON** (Binary JSON)

### **Key Characteristics**
- **Better locality than relational models** → All relevant data is stored in a single document.
- **Weaker at joins** → Cross-document joins are less efficient than SQL table joins.
- **Popular use cases** → Content management, product catalogs, and user profiles.

📌 **Example**:  
In a **relational model**, book data might be spread across **multiple tables** (title, author, reviews).  
In a **document model**, all book details are stored in a **single document**, making retrieval faster.

📌 **Key Takeaway**: **Document models are great for retrieving entire records quickly but are inefficient for complex relationships requiring joins.**

---

### **2.2 Graph Model (Nodes & Edges)**
A **graph database** stores data as **nodes (entities)** and **edges (relationships between entities)**.

### **Key Characteristics**
- **Optimized for relationships** → Queries like "How is user A connected to user B?" are more efficient.
- **Best suited for highly interconnected data** → Social networks, recommendation systems, fraud detection.
- **Graph query languages** → Graph databases use **Cypher (Neo4j)** or **Gremlin (Amazon Neptune)** instead of SQL.

📌 **Example**:  
In a **social network**, a graph model represents:
- **Users as nodes**
- **Friendships and interactions as edges**

📌 **Key Takeaway**: **Graph models prioritize relationships over individual data records, making them ideal for networked data analysis.**

---

## **📌 3. Structured vs. Unstructured Data**
### **3.1 Structured Data (Schema-Based)**
- **Follows a predefined schema** (e.g., SQL tables).
- **Stored in a data warehouse**.
- **Easy to search and analyze**.
- **Can only handle data with a specific schema**
- ***Schema changes will cause a lot of troubles**
- **Changes to schema require schema updates** → May introduce bugs.

📌 **Example**: A banking database with **structured tables** for transactions, customer records, and account details.

### **3.2 Unstructured Data (Schema-Free)**
- **No predefined schema** (e.g., raw text, images, videos).
- **Stored in a data lake**.
- **Fast arrival**
- **Can handle data from any source**
- **No need to worry about schema changes (yet), as the worry is shifted to the downstream applications that use this data**
- **Can be processed into structured data later**.

📌 **Example**: A social media platform storing **raw user posts, comments, and images** before processing them.

### **Data Warehouse vs. Data Lake**
| **Storage Type** | **Purpose** | **Schema Requirement** | **Best Use Case** |
|----------------|------------|------------------|---------------|
| **Data Warehouse** | Stores processed, structured data. | **Schema required upfront**. | Business intelligence, analytics. |
| **Data Lake** | Stores raw, unstructured data. | **Schema applied later**. | AI/ML model training, raw data storage. |

📌 **Key Takeaway**: **Data warehouses are ideal for structured analytics, while data lakes provide flexible storage for AI/ML applications.**

---

## **📌 Key Interview Questions & Answers**
### **❓ Q1: How do the relational model and document model differ in handling data relationships?**
✅ **Answer:**  
- **Relational model** → Uses **tables** with **foreign keys and joins** to manage relationships.  
- **Document model** → Stores **all related data in a single document**, optimizing for read efficiency but making joins harder.  
- **Example**: A **relational database** stores a book's metadata in one table and its reviews in another, while a **document database** stores everything in one JSON document.

---

### **❓ Q2: When would you choose a graph database over a relational database?**
✅ **Answer:**  
- **Graph databases** excel when **relationships between data points** are crucial.  
- **Use case examples**:
  - **Social networks** → Friend connections.
  - **Recommendation systems** → Product-user interactions.
  - **Fraud detection** → Identifying anomalous connections in financial transactions.
- **Key Advantage**: Graph databases perform **faster queries** for connected data compared to relational joins.

📌 **Example**: In a **fraud detection system**, a graph database can quickly find **suspicious transaction networks**, whereas a relational database would require expensive join queries.

---

### **❓ Q3: What are the trade-offs between structured and unstructured data storage?**
✅ **Answer:**  
| **Factor** | **Structured Data (Warehouse)** | **Unstructured Data (Lake)** |
|-----------|---------------------------------|-----------------------------|
| **Schema** | Predefined and rigid. | Flexible, schema applied later. |
| **Storage Cost** | Higher due to indexing. | Lower, optimized for bulk storage. |
| **Query Speed** | Faster due to indexing. | Slower; needs preprocessing. |
| **Best Use Case** | Business intelligence, analytics. | AI/ML training, raw data analysis. |

📌 **Example**: A company might store **sales reports** in a **data warehouse** (structured) and **customer support chat logs** in a **data lake** (unstructured).

---

## **📌 Key Takeaways (3-Sentence Summary)**
1️⃣ **The relational model (SQL) is best for structured, normalized data but can be inefficient for complex joins.**  
2️⃣ **NoSQL models (document and graph) optimize for flexibility and relationships but come with trade-offs in querying efficiency.**  
3️⃣ **Structured data (warehouses) is best for analytics, while unstructured data (lakes) is ideal for AI/ML applications.**  

---
