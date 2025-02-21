# ML System Design - Chapter 1.2 Summary

## 📌 Key Terms in Machine Learning Systems

### 1️⃣ **Latency**
- **Definition:** The time taken from receiving a query to returning a result.
- **In ML systems:** Latency measures the response time from sending a request to receiving a response.
- **Measurement:** Percentiles (e.g., p95, p99) are preferred over mean to avoid skew from network errors.

### 2️⃣ **Inference**
- **Definition:** The process where a trained ML model makes predictions on new or unseen data.
- **Example:** A recommendation system predicting which restaurant a user is likely to order from.

---

## 📌 1. ML in Research vs Production

Machine learning models behave differently in **research** and **production** environments. The table below outlines the key differences:

| **Aspect**         | **In Research** | **In Production** |
|--------------------|----------------|-------------------|
| **Goal**          | Achieve **state-of-the-art (SOTA)** performance on benchmark datasets. Models may be **complex, slow, or hard to interpret**. | Models must meet **real-world constraints**, balancing **speed, interpretability, and cost**. |
| **Computational Priority** | **Throughput-focused** (maximize queries processed per second). | **Latency-focused** (reduce response time). Prioritizing low latency may **increase hardware cost**. |
| **Data** | **Static** (fixed dataset for training & testing). | **Constantly changing**, possibly **biased or unstructured**. Data drift may degrade model performance. |
| **Fairness & Bias** | Usually **not a focus**. | **Crucial**. Model biases can impact fairness in **hiring, lending, healthcare**. |
| **Interpretability** | Often ignored. | **Required** to build trust, detect bias, and debug models. |

---

## 📌 2. Different Stakeholders and Conflicting Requirements
📌 **Why is ML production complex?**
- Unlike research, where the primary goal is **SOTA accuracy**, ML in production must satisfy **multiple stakeholders**, each with different and sometimes conflicting objectives.

### **Case Study: Restaurant Recommendation System**
- **Business Goal:** Recommend restaurants that increase revenue.
- **Stakeholders & Their Requirements**:
  - **ML Engineers** → Want a model that predicts **user preferences** accurately.
  - **Sales Team** → Prefer a model that recommends **expensive restaurants** to maximize service fees.
  - **Product Team** → Require **low latency (<100ms)**, as every increase in delay reduces user engagement.
  - **Infrastructure Engineers** → Want **scalable systems** that don't require frequent model retraining.
  - **Managers** → Seek to **balance all priorities** while keeping costs low.

🔹 **Key Takeaway**:  
ML Engineers **must understand and prioritize different requirements** when designing production models. Often, the best approach is **building multiple models** that address different objectives and **combining their outputs**.

---

## 📌 3. Understanding Latency Distribution
### **Why latency measurement matters?**
- Latency is **not a single value**, but a **distribution**.
- **Using percentiles (e.g., median, p95, p99) is more accurate** than mean:
  - **Mean latency can be skewed by network errors**.
  - **Higher percentiles (p95, p99) help identify system outliers, and a common practice to use high percentiles to specify the performance requirments for your system**
  
### **Practical Considerations**
- **Example:** A voice assistant (like Alexa) requires **low-latency** inference to feel responsive.
- **Batch processing in distributed systems** increases latency, as it requires **waiting for enough queries to arrive before processing**.

---

## 📌 4. Batch Processing & The Trade-Off Between Latency and Throughput
📌 **Why does batch processing increase latency?**
- **Batching is common in distributed ML systems** to improve efficiency.
- **However, it introduces additional latency**:
  - The system must **wait** for enough queries to form a batch before processing them.
  - This **increases latency but improves throughput**.

🔹 **Example**:  
| **Processing Mode** | **Latency** | **Throughput** |
|--------------------|-----------|-------------|
| **One query at a time** | Low latency | Low throughput |
| **Batch of 10 queries** | Medium latency | Higher throughput |
| **Batch of 50 queries** | High latency | Maximum throughput |

📌 **Key Trade-Off**:
- If a system **requires real-time responses** (e.g., fraud detection), **batching should be minimized**.
- If a system **handles large-scale data processing** (e.g., recommendation systems), **batching can improve efficiency**.

---

## 📌 Key Takeaways (3-Sentence Summary)
1️⃣ **ML research focuses on SOTA performance, while production prioritizes speed, interpretability, and real-world constraints.**  
2️⃣ **Latency is a critical metric in ML systems, with percentiles (p50,p95, p99) offering a more reliable measurement than mean latency.**  
3️⃣ **Batch processing can increase inference latency, but is commonly used in large-scale distributed ML systems for efficiency.**  

---

## 📌 If an Interviewer Asks...
**❓ Q1: Why is ML latency measurement important in production?**  
✅ **Answer:**  
Latency affects **user experience and system performance**. Mean latency can be **misleading**, so high percentiles (e.g., p95) help detect outliers and ensure **real-world system reliability**.

**❓ Q2: Why does ML in production prioritize interpretability?**  
✅ **Answer:**  
Interpretability is essential for **debugging, bias detection, and regulatory compliance**. In high-stakes applications like **loan approval and medical diagnosis**, a black-box model is often unacceptable.

**❓ Q3: How does batch processing affect ML inference?**  
✅ **Answer:**  
Batching **improves computational efficiency**, but introduces **higher latency**, since the system must **wait for enough queries before processing them**.

---

## 📌 Next Steps for AI Engineers 🚀
✅ **Continue mastering ML deployment, MLOps, and latency optimization**  
✅ **Experiment with model interpretability tools (SHAP, LIME)**  
✅ **Apply percentile-based latency analysis in real-world ML systems**  


