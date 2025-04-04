# 📌 Designing Machine Learning Systems - Chapter 5.1–5.2: Feature Engineering (Part 1-missing value)

## 📌 Chapter 5 Overview: What is Feature Engineering?
- **Definition**: Feature engineering is the process of selecting and transforming raw data into meaningful inputs that can be used by machine learning models.
- It determines **what information to use** and **how to represent it**.
- Effective feature engineering **improves model performance** and is often considered **more important than model choice**.

---

## 📌 5.1 Learned Features vs. Engineered Features

### **1️⃣ Classical ML (Manual Feature Engineering)**
- Common in pre-deep learning workflows.
- Requires **domain knowledge** to manually:
  - Clean and normalize data.
  - Extract meaningful features (e.g., n-grams from text).
  - Encode and vectorize features.

📌 **Example**: Spam classification before deep learning:
- Manual preprocessing: lemmatization, removing stopwords/punctuation, expanding contractions.
- Creating n-grams (e.g., bigrams).
- Building a vocabulary and mapping text to feature vectors.

### **2️⃣ Deep Learning (Learned Features)**
- Feature extraction is **partially or fully automated**.
- Steps typically include:
  - Tokenizing text.
  - Creating a vocabulary.
  - Mapping words to embeddings or one-hot vectors.
- The **neural network learns features automatically** from raw inputs (e.g., images or text).

📌 **Benefits**:
- **Reduces manual effort** and potential errors.
- **Scales better** to complex tasks.

📌 **Trade-offs**:
- Complex domains (e.g., fraud detection) may still **require expert-crafted features** to complement learned ones.

📌 **Real-World Example**:
- TikTok video recommendation may involve **millions of features**, requiring **automatic pipelines** and **feature selection systems**.

---

## 📌 5.2 Common Feature Engineering Operations (Start)

### **Handling Missing Values**
Missing values are **ubiquitous in real-world data**. But not all missing values are the same.

### **Types of Missing Data**
| Type | Description | Example |
|------|-------------|---------|
| **Missing Not at Random (MNAR)** | Missingness depends on the missing value itself. | People with **higher income** tend not to disclose it. |
| **Missing At Random (MAR)** | Missingness depends on another observed variable. | **Age** missing more often for **gender A** respondents. |
| **Missing Completely At Random (MCAR)** | No underlying reason for the missingness. | A job field left blank randomly. Rare in real-world data. |

---

### **Strategies for Handling Missing Values**

#### **1️⃣ Deletion**

- **Column Deletion**:
  - If a feature has **too many missing values** (e.g., >= 50%, depends on requirements), drop it.

- **Row Deletion**:
  - If a row has missing values and MCAR condition holds, and **very few rows are affected** (e.g., <0.1%).

📌 **Risks of Deletion**:
- **Losing important signals**.
- **Bias amplification**:
  - Deleting MNAR data removes meaningful features.
  - Deleting MAR data (e.g., all rows missing age) may exclude specific subgroups entirely.

#### **2️⃣ Imputation**

- Replace missing values with:
  - **Default values** (e.g., empty string).
  - **Mean / Median / Mode** of the feature.

📌 **Warnings**:
- Filling with possible values (e.g., fill number of children with 0) can confuse the model between **actual value** and **missingness**.
- Can cause **data leakage** or **bias injection**.
- Models may encounter **unknown imputed values during inference** if not seen during training.

📌 **Best Practices**:
- Always distinguish between "missing" and valid values (e.g., use an "unknown" flag).
- Evaluate imputation strategies through **experiments**, not assumptions.

---

## 📌 Final Takeaways (for Part 1)
1️⃣ **Deep learning has automated much of feature extraction**, but classical feature engineering is still vital in many domains.  
2️⃣ **Missing values are common and nuanced**—different types of missingness require different strategies.  
3️⃣ **Imputation and deletion come with trade-offs**, and the right choice depends on the data distribution and model requirements.  

---
# 📌 Designing Machine Learning Systems - Chapter 5.2 (b): Feature Engineering – Scaling

## 📌 Why Feature Scaling Matters

- **Feature scaling** ensures input features are on similar ranges.
- Especially important for:
  - **Distance-based models** (e.g., k-NN, SVM).
  - **Gradient-based models** (e.g., logistic regression, gradient boosting).
- **Neglecting to scale** can result in:
  - Gibberish predictions.
  - Slower or unstable convergence.
  - Models being dominated by features with larger ranges.

📌 **Key Insight**: Scaling is **simple but critical**—especially in traditional ML pipelines.

---

## 📌 Scaling Techniques

### **1️⃣ Min-Max Scaling (Normalization)**

- **Rescales values to a specific range**, commonly \([0, 1]\) or \([-1, 1]\).

#### **Formula**:
For range \([0, 1]\):
\[
x' = \frac{x - \min(x)}{\max(x) - \min(x)}
\]

For range \([a, b]\) (e.g., \([-1, 1]\)):
\[
x' = a + \frac{(x - \min(x))(b - a)}{\max(x) - \min(x)}
\]

📌 **Tip**: \([-1, 1]\) often performs better empirically than \([0, 1]\).

---

### **2️⃣ Standardization (Z-score Normalization)**

- Use when data is **approximately normally distributed** or when you **don’t want to assume bounds**.

#### **Formula**:
\[
x' = \frac{x - \mu}{\sigma}
\]
- Where:
  - \(\mu\) is the **mean** of the feature.
  - \(\sigma\) is the **standard deviation**.

📌 **Benefit**: Results in features with **mean = 0** and **std = 1**, which can improve performance in models that assume normality.

---

### **3️⃣ Log Transformation**

- Helps with **skewed distributions** (e.g., income, counts, durations).
- **Transforms data** by applying:
  \[
  x' = \log(x + 1)
  \]
  (adding 1 avoids \(\log(0)\) issues).

📌 **Use Cases**:
- Works well for **positive-only features**.
- Common in domains like **finance, health, fraud detection**.

📌 **Caution**:
- Doesn’t work for all features.
- Can affect **interpretability and downstream analysis**.

---

## 📌 Additional Considerations

### **1️⃣ Scaling and Data Leakage**
- **Scaling uses global statistics (min, max, mean, std)** from training data.
- **DO NOT** use test data to compute scaling parameters—this leads to **data leakage**.
- During inference, **reuse training stats** to transform new samples.

### **2️⃣ Scaling Drift**
- **If new incoming data distribution shifts**, original stats become stale.
- **Retrain or update scaling parameters periodically** to maintain performance.

---

## ✅ Summary: When and How to Scale Features

| **Technique** | **When to Use** | **Pros** | **Cons** |
|---------------|----------------|----------|----------|
| Min-Max Scaling | When feature bounds are known and fixed. | Simple, interpretable | Sensitive to outliers |
| Standardization | When features follow (or assumed to follow) a normal distribution. | Robust, widely supported | Affected by outliers |
| Log Transformation | When data is skewed (e.g., exponential). | Reduces skewness, improves symmetry | Only for positive values, not always effective |

📌 **Key Takeaway**: Always evaluate scaling decisions via experiments—scaling may be simple, but its impact on model performance is significant.

---

## 📌 Final Thoughts

1️⃣ **Scaling is essential for gradient-based and distance-based models**—never skip it in traditional ML.  
2️⃣ **Standardization and min-max scaling are go-to choices**, depending on your data shape.  
3️⃣ **Be aware of data leakage and drift when applying scaling in production pipelines.**

---


