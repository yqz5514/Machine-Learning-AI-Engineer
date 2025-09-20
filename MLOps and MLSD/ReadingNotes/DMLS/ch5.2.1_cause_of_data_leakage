# 📘 Designing Machine Learning Systems — Chapter 5: Feature Engineering  
## 🧪 Topic 2: Data Leakage  
### Section 1: Common Causes of Data Leakage

---

## ⚠️ What Is Data Leakage?

Data leakage occurs when **information that should not be available at training time** is used to build the model. This can result in:

- **Over-optimistic validation scores**
- **Poor generalization in production**
- **Undetected bugs until post-deployment**

Even experienced practitioners and competition winners can fall into this trap.

---

## 🔍 Common Causes of Data Leakage

### 1. Random Splitting of Temporally-Correlated Data

- **Issue**: Random splits leak future information into the training set.
- **Example**: If data from Day 7 appears in both train and test, the model can "cheat".
- **Solution**: Perform **chronological splits** (e.g., Train on Weeks 1–4, Test on Week 5).

> ✅ Use time-based splitting when data is time-dependent.  
> ❌ Avoid random splitting in time-series data.

---

### 2. Scaling Before Splitting

- **Issue**: Normalizing using global statistics leaks information from the validation/test set.
- **Solution**:
  1. **Split first**
  2. Compute normalization stats **on training data only**
  3. Apply the same transformation to validation/test data

---

### 3. Imputing Missing Values Before Splitting

- **Issue**: Imputing with global mean/median uses data from the entire dataset.
- **Solution**: Impute using only the **training set statistics**.

---

### 4. Duplicate Samples Across Splits

- **Issue**: The same or near-duplicate data appears in both train and test sets.
- **Examples**:
  - CIFAR-10: ~3.3% of test images were near-duplicates of training images.
  - Web-scraped datasets often contain duplicates.
- **Solution**:
  - **Deduplicate before splitting**
  - Also verify splits after dividing
  - Oversample *after* the split to avoid reintroducing duplicates

---

### 5. Group Leakage (Correlated Samples)

- **Issue**: Samples from the same source (e.g., patient, object, session) leak into different splits.
- **Examples**:
  - Two CT scans from the same patient
  - Images captured in quick succession
- **Solution**: 
  - Group by identifier (e.g., `patient_id`, `session_id`)
  - Ensure group-level separation across train/val/test

---

### 6. Leakage from Data Collection or Generation Process

- **Issue**: Hidden metadata or artifacts in the data are unintentionally correlated with the label.
- **Example**: 
  - A certain CT machine is used only for suspected cancer patients → model learns machine ID, not cancer indicators.
- **Solution**:
  - Normalize sources (e.g., image size, scanner metadata)
  - Consult domain experts (SMEs)
  - Audit data pipeline and metadata

---

## 📉 Real-World Example: Kaggle Ion Switching Competition (2020)

- Test labels were **accidentally leaked** via synthetic data patterns.
- Top teams reverse-engineered the leak and **exploited it** to win.
- Takeaway: Even public benchmarks can suffer from leakage. Always validate assumptions.

---

## ✅ Summary of Prevention Strategies

| Cause                           | Recommended Fix                                     |
|--------------------------------|-----------------------------------------------------|
| Temporal correlation           | Use time-based split                                |
| Scaling with global stats      | Compute stats only from train set                   |
| Global imputation              | Use train-only statistics                           |
| Duplicate entries              | Deduplicate before/after splitting                  |
| Group leakage                  | Split based on group ID                             |
| Generation process artifacts   | Normalize sources, involve SMEs, audit pipelines    |

---

## 💡 Key Takeaways

- **Data leakage can invalidate your entire ML pipeline.**
- Prevention requires **rigorous data practices** and **domain understanding**.
- Watch out for **hidden correlations**, **implicit metadata**, and **preprocessing mistakes**.

---
