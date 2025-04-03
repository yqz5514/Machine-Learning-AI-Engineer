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


