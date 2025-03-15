# 📌 Designing Machine Learning Systems - Chapter 4.3: Class Imbalance

## **📌 What is Class Imbalance?**
- **Definition**: Class imbalance occurs when there is a **significant difference** in the number of samples per class in a dataset.
- **Common in classification tasks**, but also exists in **regression tasks** with **skewed label distributions**.

📌 **Example (Classification)**:
- **Fraud detection**: The majority of credit card transactions are **non-fraudulent**, making fraud cases extremely rare.
- **Churn prediction**: Most users continue using a service, while only a few churn.
- **Disease screening**: The vast majority of people **do not** have a terminal illness.

📌 **Example (Regression)**:
- **Predicting healthcare bills**: Most medical bills are **low**, but a small number of patients have **extremely high** costs.
  - A 100% error in predicting **a $250 bill** (actual $500, predicted $250) is acceptable.
  - A 100% error in predicting **a $10,000 bill** (actual $20,000, predicted $10,000) is **not acceptable**.

📌 **Key Takeaway**: **Class imbalance can degrade model performance by biasing predictions towards majority classes.**

---

## **📌 4.3.1 Challenges of Class Imbalance**
Class imbalance **makes model training difficult** for **three reasons**:

### **1️⃣ Insufficient Signal for Minority Classes**
- ML models learn better when **each class has sufficient training examples**.
- With **highly imbalanced data**, the model struggles to **generalize minority class patterns**.

### **2️⃣ Model Overfitting to Majority Classes**
- The model can exploit **simple heuristics** rather than learning meaningful patterns.
- Example:  
  - In **fraud detection**, if 99.9% of transactions are **legitimate**, the model can simply **predict "not fraud" for all cases** and still achieve **99.9% accuracy**.

### **3️⃣ Asymmetric Costs of Errors**
- **False negatives on minority classes** can be **more costly** than false positives.
- Example:  
  - **Misclassifying a cancer case as "no cancer" is worse** than misclassifying a healthy patient as "cancer" (who can undergo further testing).
  - **Predicting a $50,000 medical bill as $10,000** is worse than **predicting a $250 bill as $500**.

📌 **Key Takeaway**: **Models tend to ignore minority classes, leading to biased predictions and higher misclassification costs.**

---

## **📌 4.3.2 Handling Class Imbalance**
There are **three major approaches** to address class imbalance:

1. **Choosing the Right Evaluation Metrics**  
2. **Data-Level Methods (Resampling Techniques)**  
3. **Algorithm-Level Methods (Loss Function Adjustments)**  

---

### **1️⃣ Choosing the Right Evaluation Metrics**
- **Accuracy is misleading** in imbalanced datasets.
- **Better metrics**:
  - **Precision & Recall**: Useful for rare event detection.
  - **F1 Score**: Balances precision and recall.
  - **AUROC (Area Under the ROC Curve)**: Measures model effectiveness across different thresholds.
  - **PR AUC (Precision-Recall Curve)**: Better for highly imbalanced datasets.

📌 **Example**:
- A model with **99.9% accuracy** in fraud detection **might not detect any fraud cases**.
- **F1-score and Recall** help evaluate **true performance on minority classes**.

---

### **2️⃣ Data-Level Methods: Resampling**
**Resampling modifies the training data distribution** to reduce class imbalance.

| **Method** | **Description** | **Risk** |
|-----------|---------------|---------|
| **Oversampling** | Duplicate or generate more samples from the minority class. | Overfitting (model memorizes duplicated data). |
| **Undersampling** | Remove samples from the majority class to balance the dataset. | Loss of valuable data from the majority class. |
| **SMOTE (Synthetic Minority Oversampling Technique)** | Generates synthetic data points by interpolating between minority samples. | Works well for **low-dimensional data**, but struggles in **high-dimensional feature spaces**. |
| **Dynamic Sampling** | During training, oversample low-performing classes and undersample high-performing classes. | Requires **continuous model evaluation** to adjust sampling. |

📌 **Key Takeaway**: **Resampling techniques help balance datasets, but must be carefully applied to prevent overfitting or information loss.**

---

### **3️⃣ Algorithm-Level Methods: Adjusting Loss Functions**
Instead of modifying the data, we **modify the loss function** to make the model more robust to class imbalance.

#### **A. Cost-Sensitive Learning**
- Assigns **higher weights to minority class instances** during training.
- If **misclassifying fraud costs more than misclassifying a normal transaction**, the model **prioritizes fraud detection**.

📌 **Example**:
- **Credit card fraud detection**:  
  - Weight fraudulent transactions **10x more** than normal transactions in the loss function.

---

#### **B. Class-Balanced Loss**
- **Adjusts loss based on class frequencies**:  
  - The fewer samples a class has, **the higher its weight** in the loss function.
- **Formula**:
  In its vanilla form, we can make the weight of each class inversely proportional to the number of samples in that class, so that the rarer classes have higher weights. In the following equation, N denotes the total number of training samples:

  <img width="293" alt="image" src="https://github.com/user-attachments/assets/6fc7f8cc-27a3-4ef6-81ce-7485d72bed86" />
The loss caused by instance x of class i will become as follows, with Loss(x, j) being the loss when x is classified as class j. It can be cross entropy or any other loss function.

  <img width="344" alt="image" src="https://github.com/user-attachments/assets/f7a3c83a-b6d4-493a-b34e-c6a2b18ce9f3" />

- Prevents **majority class dominance**.

📌 **Example**:
- **Resume screening models**: If 98% of applicants are rejected, increase the weight of **hired candidates** so the model learns from them.

---

#### **C. Focal Loss**
- Reduces the loss for **easily classified samples**, and **increases focus on harder cases**.
- If a model **already classifies a sample correctly with high confidence**, it **reduces its loss weight**.
- Useful for **imbalanced object detection tasks**.
  
<img width="586" alt="Screenshot 2025-03-13 at 10 34 05 AM" src="https://github.com/user-attachments/assets/5b467c91-814f-4c21-988e-c1e66840b240" />

📌 **Example**:
- In **medical image classification**, the model may **focus more on rare cancer cases** rather than easy-to-classify normal images.

---

## **📌 Summary: Methods to Handle Class Imbalance**
| **Approach** | **Method** | **Pros** | **Cons** |
|------------|------------|------------|------------|
| **Evaluation Metrics** | Precision, Recall, F1, AUROC, PR AUC | Provides a better assessment of rare-class performance | Does not modify the model/data |
| **Resampling (Data-Level)** | Oversampling, Undersampling, SMOTE, Dynamic Sampling | Modifies dataset to balance class distributions | May cause overfitting (oversampling) or data loss (undersampling) |
| **Loss Adjustments (Algorithm-Level)** | Cost-sensitive learning, Class-balanced loss, Focal loss | Directly optimizes model for class imbalance | Requires careful tuning of loss weights |

📌 **Key Takeaway**: **A combination of resampling and algorithm-level adjustments often yields the best results.**

---

## **📌 Final Takeaways (3-Sentence Summary)**
1️⃣ **Class imbalance biases models toward majority classes, leading to poor performance on minority classes.**  
2️⃣ **Resampling (oversampling, undersampling, SMOTE) modifies the dataset to address imbalance, while loss function adjustments (cost-sensitive learning, class-balanced loss, focal loss) modify how the model learns.**  
3️⃣ **Using the right evaluation metrics (F1, PR AUC) ensures fair model assessment and prevents misleading accuracy results.**  

---
## **📌 Interview Questions & Answers: Class Imbalance in Machine Learning**

### **❓ Q1: Why is accuracy a misleading metric for imbalanced classification problems?**
✅ **Answer:**  
- In an imbalanced dataset, the model can **achieve high accuracy by always predicting the majority class**.
- Example:  
  - In a **fraud detection system**, if 99.9% of transactions are **non-fraudulent**, a model that **always predicts "not fraud" will be 99.9% accurate** but completely useless.
- **Better alternatives**:
  - **Precision & Recall**: Helps evaluate how well the model detects minority classes.
  - **F1 Score**: Balances precision and recall.
  - **PR AUC (Precision-Recall Curve)**: Preferred when the minority class is extremely rare.

📌 **Key Takeaway**: **Accuracy alone does not reflect a model’s performance in imbalanced datasets—metrics like Precision, Recall, and F1-score should be used instead.**

---

### **❓ Q2: What are the differences between oversampling, undersampling, and SMOTE in handling class imbalance?**
✅ **Answer:**  
| **Method** | **Description** | **Pros** | **Cons** |
|-----------|---------------|--------|---------|
| **Oversampling** | Duplicates or generates more samples from the minority class. | Ensures minority class is well-represented. | Can lead to **overfitting**. |
| **Undersampling** | Removes some majority class samples to balance data. | Reduces dataset size, improving efficiency. | Risk of **losing valuable information**. |
| **SMOTE (Synthetic Minority Oversampling Technique)** | Creates **synthetic samples** by interpolating between existing minority class samples. | Avoids overfitting seen in regular oversampling. | **Struggles in high-dimensional feature spaces**. |

📌 **Key Takeaway**: **SMOTE is a better alternative to naive oversampling, but resampling techniques should be combined with proper model evaluation strategies to prevent bias.**

---

### **❓ Q3: What are some algorithm-level techniques to handle class imbalance in machine learning models?**
✅ **Answer:**  
1. **Cost-Sensitive Learning** → Assigns **higher weights to minority class samples** to make misclassification costlier.
2. **Class-Balanced Loss** → Modifies loss function based on class frequencies:
   \[
   \text{Loss}(x, j) = \frac{1}{\text{Frequency of Class } j}
   \]
   - **Rare classes contribute more to loss**, preventing bias toward majority class.
3. **Focal Loss** → **Focuses learning on hard-to-classify samples** by reducing loss for already well-classified samples.
   - Used in **imbalanced object detection** and **medical diagnosis** tasks.

📌 **Example**:  
- In a **resume screening system**, if **98% of applicants are rejected**, using **class-balanced loss** ensures that the model learns more from the **hired candidates** instead of ignoring them.


