# Designing Machine Learning Systems - Chapter 2 Summary

## 📌 Introduction to Machine Learning Systems Design
ML system design takes a **holistic approach** to MLOps, considering all components:
- **Business objectives**
- **Data stack**
- **Infrastructure**
- **Deployment**
- **Monitoring**

Before developing an ML system, we must **understand business needs**, define **ML-specific objectives**, and establish **core system requirements**:  
✅ **Reliability**  
✅ **Scalability**  
✅ **Maintainability**  
✅ **Adaptability**

---

## 📌 1. Business vs. ML Objectives
### **Aligning ML Metrics with Business Goals**
- **Data scientists** focus on ML metrics (e.g., accuracy, F1 score, latency).
- **Businesses** focus on **profitability, user engagement, and cost savings**.

**Example**:  
- A **0.2% improvement in click-through rate (CTR) for a recommender system** can **increase e-commerce revenue by millions**.
- Netflix uses **take-rate** (quality plays / total recommendations) as an ML metric linked to **streaming hours and subscription rates**.

📌 **Key Takeaway**:  
For an ML project to succeed in a company, its **performance must directly impact business metrics**.

---

## 📌 2. Requirements for ML Systems
A well-designed ML system must meet four key requirements:

### **1️⃣ Reliability**
- **Definition**: The system should function correctly under different conditions.
- **Challenge**: ML failures are often **silent** (e.g., incorrect Google Translate results).
- **Best Practices**:
  - Monitor models for **drift & bias**.
  - Use **human-in-the-loop systems** for critical applications.

---

### **2️⃣ Scalability**
An ML system must scale in three ways:
1. **Model Complexity**:  
   - E.g., moving from a logistic regression to a **100M parameter neural network**.
2. **Traffic Volume**:  
   - Handling **10,000 → 10M requests/day** requires **dynamic scaling**.
3. **Model Count**:  
   - Some AI startups serve **one model per enterprise customer**, scaling to **8,000+ models**.

📌 **Scalability Strategies**:
- **Auto-scaling infrastructure** (e.g., Kubernetes, AWS Auto Scaling).
- **Efficient model management** (versioning, monitoring).
- **Cloud resource optimization** to **minimize operational costs**.

---

### **3️⃣ Maintainability**
An ML system should be **collaborative** and **reproducible**:
- **Multi-team workflows** (ML engineers, MLOps, DevOps).
- **Version control** for **code, data, and models**.
- **Clear documentation** to ensure **long-term maintainability**.

🚀 **Key Practice**:  
Use **MLflow** or **Weights & Biases** for **experiment tracking & model versioning**.

---

### **4️⃣ Adaptability**
ML systems **must evolve** to handle:
- **Changing business requirements**.
- **Data distribution shifts** (concept drift).
- **Regulatory updates**.

📌 **Continuous Learning Strategies**:
- **Automated retraining** pipelines.
- **Monitoring for drift detection** (e.g., using **Evidently AI**).
- **User feedback loops** to improve model robustness.

---

## 📌 3. The Iterative ML Development Process
Developing an ML system **is never a one-off task**—it’s an **iterative cycle**:

### **1️⃣ Project Scoping**
- Define **objectives, constraints, and stakeholders**.
- Estimate **resources (data, compute, budget)**.

### **2️⃣ Data Engineering**
- Handle **structured & unstructured data**.
- **Generate & clean labeled datasets**.

### **3️⃣ ML Model Development**
- Feature engineering, model selection, training, and evaluation.

### **4️⃣ Deployment**
- Convert ML models into **production-ready APIs**.
- Optimize **latency vs. throughput trade-offs**.

### **5️⃣ Monitoring & Continuous Learning**
- Detect **model drift** and **data pipeline failures**.
- Implement **real-time feedback loops**.

### **6️⃣ Business Impact Analysis**
- Assess **model impact on KPIs (Key Performance Indicators)**.
- Iterate based on **business & user feedback**.

📌 **Key Takeaway**:  
ML system development is **cyclical**—monitoring, updating, and improving models **never stops**.

---

## 📌 4. Framing ML Problems
ML problems must be well-defined **before choosing an algorithm**:
- **Inputs & outputs** must be clear.
- **The problem must be ML-solvable** (not all problems need ML).

📌 **Example**:
- **Customer Support AI**:  
  - Instead of using ML for **general speed improvement**, frame it as a **classification problem**:
  - **Input**: Customer query → **Output**: Route to the correct department.

---

## 📌 5. Types of ML Tasks
### **Classification vs. Regression**
| **Task Type** | **Example** |
|--------------|------------|
| **Classification** | Email spam detection (Spam / Not Spam) |
| **Regression** | Predicting house prices (continuous output) |

📌 **Framing Consideration**:
- **Classification can be reframed as regression** (e.g., probability scoring).
- **High-cardinality problems (many labels) require hierarchical classification**.

---

## 📌 6. Objective Functions & Multi-Objective Optimization
**An ML system needs an objective function to learn.**
- **Supervised ML**: Loss = Ground truth vs. Prediction
- **Common Loss Functions**:
  - **Regression**: RMSE, MAE
  - **Classification**: Cross-entropy, F1-score

### **Decoupling Objectives**
If an ML system must **balance multiple goals**, separate objectives into **independent models**.

📌 **Example: AI News Feed Ranking**
1. **Quality Model** → Filters **spam/misinformation**.
2. **Engagement Model** → Prioritizes **high-click-rate posts**.
3. **Final Ranking** = `α * quality_score + β * engagement_score`

🚀 **Advantage**:  
Tuning `α` & `β` allows **adjustment without retraining** models.

---

## 📌 7. Mind vs. Data: The AI Debate
### **Two opposing views in ML progress**:
1. **Mind-first (Architectural Design)**:  
   - Turing Award winner **Judea Pearl** → “Data is dumb, intelligent algorithms are the future.”
   - AI should rely more on **causal inference & reasoning**.
2. **Data-first (Scalability & Compute Power)**:  
   - **Google & OpenAI** → “We don’t have better algorithms, just more data.”
   - **Deep Learning breakthroughs** (GPT, BERT) were **data-driven**.

🚀 **Key Insight**:
- **Both architectural design & massive data are crucial**.
- **The trend favors scaling up models with more data** (e.g., GPT-3 → GPT-4).

---

## 📌 Key Takeaways (3-Sentence Summary)
1️⃣ **ML system design requires aligning business goals with ML metrics, ensuring reliability, scalability, maintainability, and adaptability.**  
2️⃣ **The ML lifecycle is iterative, requiring continuous monitoring, retraining, and business impact analysis.**  
3️⃣ **Balancing multiple objectives in ML (e.g., quality vs. engagement) is best achieved through separate models rather than optimizing a single loss function.**  

---

## 📌 Next Steps 🚀
✅ **Deep dive into data engineering (next chapter focus).**  
✅ **Apply iterative ML system design principles in real-world projects.**  
✅ **Experiment with auto-scaling, monitoring, and optimizing AI pipelines.**  

