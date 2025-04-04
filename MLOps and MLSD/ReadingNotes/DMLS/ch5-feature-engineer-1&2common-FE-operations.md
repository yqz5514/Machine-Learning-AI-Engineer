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

# 📌 Designing Machine Learning Systems - Chapter 5.2 (c): Discretization

### **This technique is included in this book for completeness, though in practice, I’ve rarely found discretization to help.**

## 📌 What is Discretization?

- **Discretization** (also called **quantization** or **binning**) is the process of converting a **continuous variable into discrete buckets**.
- It's typically used to **simplify learning**, especially when:
  - You have **limited training data**.
  - The model struggles to generalize over **small numeric differences**.

📌 **Example**:  
If the model has seen incomes like `$150,000`, `$50,000`, `$100,000` during training, and sees `$9,000.50` during inference, it might fail to understand that `$9,000.50` is closer to `$10,000` than `$150,000`.

---

## 📌 Why Use Discretization?

- Models **don’t inherently understand numeric similarity** (e.g., $9,000.50 ≠ $10,000 unless encoded or transformed).
- Grouping values into **coarse categories** reduces the model's burden of learning from infinitely many values.
- More useful when **training data is small or sparse**.

📌 **Income Grouping Example**:
| Bucket | Rule |
|--------|------|
| Low Income | < $35,000/year |
| Middle Income | $35,000–$100,000/year |
| High Income | > $100,000/year |

---

## 📌 Discretization Can Also Apply to Discrete Features

- Although designed for continuous features, **discretization can also apply to discrete features**.
- **Example – Age Buckets**:
  - < 18  
  - 18–22  
  - 22–30  
  - 30–40  
  - 40–65  
  - > 65  

📌 **Why?**  
To reduce feature complexity or align with **real-world semantics** (e.g., age groups in demographic models).

---

## ⚠️ Drawbacks of Discretization

1. **Information Loss at Boundaries**:
   - `$34,999` and `$35,000` end up in different buckets—even though they are only $1 apart.
   - Conversely, `$35,000` and `$100,000` may be in the same bucket—though far apart.

2. **Choosing Cutoffs is Hard**:
   - Requires **manual design** or domain expertise.
   - May introduce **bias** or reduce model granularity.
   - Use **histograms** and **quantiles** to guide boundaries.

3. **Discontinuity**:
   - Model sees **sudden jumps in input values**, which may hurt smooth decision boundaries.

---

## ✅ Best Practices

- **Use with caution**—only if:
  - The model is simple.
  - Training data is small.
  - Interpretability is prioritized.
- **Visualize distributions** to inform cutoff choices.
- Consider **automated binning strategies**:
  - Equal-width bins.
  - Equal-frequency bins.
  - Decision-tree–based binning.

---

## 📌 Final Takeaways (3-Sentence Summary)

1️⃣ **Discretization converts continuous features into buckets to simplify model learning**, especially in low-data regimes.  
2️⃣ **Though useful, it introduces discontinuities and may obscure important variations in input values**.  
3️⃣ **Use visualization, quantiles, or domain knowledge to set meaningful boundaries—and apply it thoughtfully**.

---

# 📌 Designing Machine Learning Systems - Chapter 5.2 (d): Encoding Categorical Features

## 📌 Why Encoding Categorical Features Matters

- **Categorical features** must be transformed into **numerical representations** to be used in ML models.
- Many beginners assume categories are **static**, but in production, **categories evolve over time**:
  - New product brands, users, IPs, restaurants, domains, etc. appear frequently.
  - Models must **generalize to unseen categories** or risk failing in production.

📌 **Key Insight**: A robust encoding strategy must handle both **known** and **new/unseen** categories.

---

## 📌 Common Pitfalls in Categorical Encoding

### **1️⃣ Static Encoding**
- Assigning **each unique category a unique ID** (e.g., Brand A → 0, Brand B → 1, …).
- **Fails in production** when:
  - New categories appear that the model hasn’t seen.
  - Unseen categories cause **model crashes or degraded performance**.

### **Real-World Example: Amazon**
- Over 2 million brands exist.
- You encode brands from `0` to `1,999,999`, but when a **new brand appears**, the model fails.
- Fix: Add an **`UNKNOWN` category** to catch all unseen brands.

---

## 📌 Problems with the UNKNOWN Category

- If `UNKNOWN` is **not seen during training**, the model won’t learn how to treat it.
- Sellers complain their **new products don’t get recommended**.
- You update the strategy:
  - Encode **top 99% most common brands**.
  - Encode **bottom 1% + all unseen brands** as `UNKNOWN`.

📌 **Still Not Enough**:
- New brands (some important) are lumped together as "UNKNOWN".
- Model treats **popular new brands** like **irrelevant or spammy ones**.

---

## 📌 Generalization Issues with Static Binning

- The issue is **not unique to Amazon**:
  - Spam detection: new users, new websites.
  - E-commerce: new product categories.
  - Any feature involving dynamic entities (e.g., IPs, accounts, URLs).

📌 **Challenge**: How do you meaningfully represent **new categories** without re-training your model?

---

## 📌 The Hashing Trick

- **Solution**: Use a **hash function** to encode categories into fixed-size buckets.
- Popularized by **Vowpal Wabbit**, also used in **scikit-learn**, **TensorFlow**, **Gensim**.

### **How it works**:
1. Apply a hash function to the category name.
2. Use the **modulo** operation to map the hash to a fixed integer range.
3. All categories (even new ones) are **guaranteed to be mapped** to a numeric index.

📌 **Example**:
- Choose a hash space of `2^18 = 262,144`.
- Any new or unseen category gets mapped to an index in `[0, 262,143]`.

---

## 📌 Pros and Cons of Hashing

| **Pros** | **Cons** |
|----------|----------|
| Handles unseen categories gracefully. | **Hash collisions**: Two categories may map to the same index. |
| Avoids model crashes in production. | Loss of interpretability. |
| Works well in online learning. | Collisions can slightly degrade performance. |

📌 **Good News**:
- Research (e.g., Booking.com) shows that even with **50% collisions**, the **performance drop is < 0.5%**.
- Can use **locality-sensitive hashing** if similarity preservation is important.

---

## 📌 Best Practices

- Use **hashing** for features with:
  - A **large number of unique categories**.
  - **High turnover rate** (e.g., accounts, URLs).
- Keep hash space **large enough** to minimize collisions.
- Monitor for **drift in category distribution** over time.

---

## 📌 Final Takeaways (3-Sentence Summary)

1️⃣ **Production ML systems must handle unseen categorical values**, which static encodings cannot reliably support.  
2️⃣ The **hashing trick** offers a scalable solution by mapping all categories (even new ones) into a fixed feature space.  
3️⃣ Though it introduces some collisions, hashing performs well in practice and is widely used in modern ML pipelines.

---
