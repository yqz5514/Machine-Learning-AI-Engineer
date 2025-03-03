# 📌 Designing Machine Learning Systems - Chapter 4.1: Sampling

## **📌 The Role of Sampling in ML Systems**
### **1️⃣ Why Is Sampling Necessary?**
- **Data in production is infinite and non-stationary**, while **datasets used for ML training are finite and static**.
- **Sampling is used throughout the ML lifecycle**:
  - **Selecting training data** from real-world data.
  - **Creating train/validation/test splits** from a dataset.
  - **Monitoring ML models** by sampling logged data for analysis.
- **Sampling is essential when**:
  - **Access to all real-world data is not possible**.
  - **Processing the full dataset is too resource-intensive**.
  - **Quick experimentation is needed** before large-scale model training.

📌 **Key Takeaway**: **Sampling balances efficiency, cost, and accuracy but requires careful selection to avoid bias.**

---

## **📌 4.1.1 Nonprobability Sampling**
Nonprobability sampling **does not use probability-based selection**.  
🔹 **Pros**: Quick and easy for initial data collection.  
🔹 **Cons**: High selection bias.

| **Sampling Method** | **Description** | **Example Use Case** |
|------------------|-----------------|------------------|
| **Convenience Sampling** | Selects data based on availability. | Scraping Wikipedia or Reddit for NLP datasets. |
| **Snowball Sampling** | Expands dataset based on existing samples. | Scraping Twitter by following accounts of known users. |
| **Judgment Sampling** | Experts manually select data points. | Handpicking examples for AI fine-tuning. |
| **Quota Sampling** | Ensures each subgroup has a fixed sample size. | Collecting equal survey responses across age groups. |

📌 **Example Bias Issue**:  
- **Self-driving car datasets** initially came from Phoenix, Arizona, and the Bay Area, creating biases in road conditions and driving behaviors.

---

## **📌 4.1.2 Simple Random Sampling**
- Every sample has an **equal probability** of being selected.
- **Pros**: Simple and unbiased.
- **Cons**: Rare categories may be **underrepresented**.

📌 **Example**:  
- If **fraudulent transactions** make up only **0.01%** of data, randomly selecting **1% of the dataset** might exclude fraud cases entirely.
- The model could then **fail to recognize fraud cases**.

---

## **📌 4.1.3 Stratified Sampling**
- The dataset is first **divided into relevant groups (strata)**.
- Then, **samples are drawn separately from each group**.

### **📌 Why Use Stratified Sampling?**
- **Ensures rare categories are represented**.
- **Balances class distributions** for model training.

📌 **Example**:  
- In **fraud detection**, if **only 5% of transactions** are fraudulent, stratified sampling ensures **both fraudulent and non-fraudulent samples** are included.

🔹 **Challenge**:  
- Hard to implement in **multi-label classification** where samples **belong to multiple categories**.

---

## **📌 4.1.4 Weighted Sampling**
- Assigns **weights to samples**, adjusting selection probabilities.
- Useful when **training data has a different distribution from real-world data**.

📌 **Example**:  
- **Weighted sampling in NLP**:
  - If a dataset has **80% English** and **20% low-resource languages**, weighted sampling **increases selection probability of low-resource languages**.
  - Prevents the model from **overfitting to English**.

🔹 **Related Concept**: **Sample Weights in ML Models**  
- **Weighted sampling**: Adjusts **which data points are selected**.
- **Sample weights**: Adjusts **how much each sample contributes to training loss**.

---

## **📌 4.1.5 Reservoir Sampling**
Reservoir sampling is used for **streaming data**, where the dataset size is **unknown** in advance.

### **📌 How It Works**
1. **Initialize a "reservoir" of size k** (e.g., store the first k samples).
2. For each **incoming nth sample**:
   - Generate a random number **i** between **1 and n**.
   - If **i ≤ k**, replace the ith element in the reservoir with the nth element.
   - Otherwise, discard the nth element.
   - Ensure have equal p = k/n on the following data selection.
3. Ensures **equal probability of selection**, even with an unknown total dataset size.

📌 **Example Use Case**:  
- Sampling tweets from **a continuous Twitter data stream**.
- Monitoring **real-time logs** in an ML system.

🔹 **Key Benefit**:  
- **Memory-efficient** → Can sample from massive datasets **without storing all data in memory**.

---

## **📌 4.1.6 Importance Sampling**
Importance sampling is used **when sampling from one distribution while training on another**.
It allows us to sample from a distribution when we only have access to another distribution

- **Bridges the gap between biased training data and real-world data**.
- Adjusts for **distribution mismatches**.
- So you sample x from Q(x) instead and weigh this sample by  p(x)/Q(x). Q(x) is called the proposal distribution or the importance distribut![image](https://github.com/user-attachments/assets/503b2058-0f79-49d0-87f2-1cdb207db3bc)
- The following equation shows that in expectation, x sampled from P(x) is equal to x sampled from Q(x) weighted by P(x)/Q(x):
- <img width="468" alt="image" src="https://github.com/user-attachments/assets/5aea2afc-9e87-4d1b-ac5b-9c4ecbf10486" />

📌 **Example**:  
- **Ad click prediction models** often overrepresent **high-budget ad campaigns**.
- **Importance sampling** can reweight smaller campaigns **to improve generalization**.

🔹 **Use Cases**:
- **Rebalancing datasets** with skewed distributions.
- **Reinforcement Learning (RL)** → Used in **policy-based RL to prioritize important experiences**.

---

## **📌 Summary: Sampling Methods for ML Training Data**
| **Sampling Method** | **Best Use Case** | **Key Limitation** |
|----------------|-------------------|------------------|
| **Nonprobability Sampling** | Quick initial dataset collection. | High selection bias. |
| **Simple Random Sampling** | Large-scale datasets with uniform distributions. | Rare categories may not appear. |
| **Stratified Sampling** | Ensuring class balance in training data. | Hard for multi-label tasks. |
| **Weighted Sampling** | Adjusting for dataset bias, handling imbalanced data. | Requires domain expertise. |
| **Reservoir Sampling** | Streaming data, online sampling. | Cannot ensure specific category selection. |
| **Importance Sampling** | Bridging distribution mismatches, reinforcement learning. | Computationally intensive. |

📌 **Key Takeaway**: **Choosing the right sampling method depends on dataset size, distribution, and task requirements.**

---

## **📌 Key Interview Questions & Answers**
### **❓ Q1: Why is simple random sampling not always the best choice for ML training data?**
✅ **Answer:**  
- **Equal probability selection** can **miss rare categories**.
- In **fraud detection**, a rare class **(0.01%) may not appear in a 1% sample**.
- **Stratified or weighted sampling** ensures rare classes are included.

---

### **❓ Q2: How does reservoir sampling work for streaming data?**
✅ **Answer:**  
- Maintains a **fixed-size sample (k) from an infinite stream**.
- Each new sample **has a decreasing probability of selection**.
- If selected, it replaces an existing sample in the **reservoir**.

📌 **Example**: Used for **sampling tweets in real-time** or **monitoring production logs**.

---

### **❓ Q3: What is the difference between weighted sampling and sample weights in ML?**
✅ **Answer:**  
- **Weighted sampling** → Controls **how data points are selected**.
- **Sample weights** → Adjust how much a data point contributes to **model training loss**.

📌 **Example**: In NLP, **weighted sampling** ensures **rare languages are selected**, while **sample weights** adjust how much they influence the final model.

---

## **📌 Final Takeaways (3-Sentence Summary)**
1️⃣ **Sampling is a critical step in ML workflows, affecting dataset representativeness and model performance.**  
2️⃣ **Different methods (stratified, weighted, reservoir) address specific challenges like class imbalance and streaming data.**  
3️⃣ **Selecting the right sampling method helps mitigate bias, optimize efficiency, and improve real-world model generalization.**  

---
