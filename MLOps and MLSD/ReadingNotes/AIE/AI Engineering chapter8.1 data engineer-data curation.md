# 📌 AI Engineering - Chapter 8.1 Summary: Data Engineer - Data Curation

## 📌 AI Engineering vs. ML Engineering: The Data Perspective  
From a data engineering perspective, **AI Engineering (AIE) and ML Engineering (MLE)** differ in their dataset focus:

- **AIE**: The goal of **dataset engineering** is to create a dataset that enables training the best model **within a given budget**.
- **MLE**: Model performance is improved through model architecture, algorithm optimization, and hyperparameter tuning.

### **Data-Centric AI vs. Model-Centric AI**
| **Approach** | **Description** | **Key Focus** |
|-------------|----------------|--------------|
| **Model-Centric AI** | Improves AI performance by enhancing models. | ✅ **New architectures**, larger models, advanced training techniques. |
| **Data-Centric AI** | Improves AI performance by optimizing data. | ✅ **Better data processing, higher-quality datasets**, fewer resources required. |

📌 **Key Takeaway**: **Both model and data improvements are necessary for meaningful AI progress**.

---

## **📌 1. Data Curation**  
Data curation is a **scientific process** that involves understanding **how models learn** and determining **what data is needed** for different training phases.  

### **Different Training Phase Data Requirements**
| **Training Phase** | **Required Data Format** |
|------------------|------------------|
| **Self-supervised fine-tuning** | Sequences of data. |
| **Instruction fine-tuning** | (Instruction, Response) pairs. |
| **Preference fine-tuning** | (Instruction, Winning Response, Losing Response) triplets. |

📌 **Key Takeaway**: **Training data should exhibit the behaviors you want your model to learn**.

### **Removing Data to Unlearn Bad Behaviors**
Data curation is not just about **adding** data but also about **removing** harmful or undesirable behaviors.  
Example: If a chatbot like **ChatGPT** is found to be arrogant, we may **remove or adjust** training data that led to such behavior.

### **Three Key Criteria for Data Curation**
1. **Data Quality** → Ensuring high-quality, well-annotated, and reliable data.
2. **Data Coverage** → Having sufficient diversity in data.
3. **Data Quantity** → Ensuring an appropriate volume of data.

---

## **📌 2. Data Quality**
A **small amount of high-quality data** often outperforms **a large amount of noisy data**.

### **Six Characteristics of High-Quality Data**
| **Characteristic** | **Description** |
|------------------|----------------|
| **Relevant** | Training examples should be relevant to the task. |
| **Aligned** | Annotations should align with the task's requirements. |
| **Consistent** | Annotations should be consistent across examples and annotators. |
| **Correctly formatted** | All examples should follow the expected format. |
| **Unique** | Avoid duplicate examples to prevent bias and data contamination. |
| **Compliant** | Data should comply with legal and regulatory standards. |

📌 **Example**: **Llama 3** researchers found that **AI-assisted annotations** were more reliable than human-generated data for safety policies.

---

## **📌 3. Data Coverage (Diversity)**
Different applications require **different dimensions of diversity**:

- **A global chatbot** → Needs **linguistic and cultural diversity**.
- **A financial AI model** → Needs **domain-specific diversity**.

📌 **Key Insight**: **Meta’s Llama 3 model improved by annealing (gradually adjusting learning rate) on high-quality code and math data**.

### **Choosing the Right Data Mix**
Two main strategies:
1. **Reflect real-world usage** → Choose a mix similar to application data.
2. **Experiment-based selection** → Run **scaling law experiments** to predict the best mix.

📌 **Example**: Meta trained **small models on candidate data mixes** to predict the best data composition for **large models**.

---

## **📌 4. Data Quantity**
Large datasets are essential for **training foundation models**, but their impact varies.

| **Model** | **Training Dataset Size** |
|-----------|--------------------------|
| **Llama 2** | **2 trillion** tokens |
| **Llama 3** | **16 trillion** tokens |

📌 **Key Takeaway**: **Fine-tuning is often more efficient than training from scratch, but too much data can lead to "ossification" (rigid model weights).**

### **Factors That Influence Data Volume Needs**
| **Factor** | **Impact** |
|-----------|-----------|
| **Fine-tuning technique** | Full fine-tuning requires more data than **LoRA or PEFT**. |
| **Task complexity** | Simple tasks (e.g., sentiment classification) need less data than complex ones (e.g., financial Q&A). |
| **Base model performance** | Larger pre-trained models need fewer fine-tuning examples. |

📌 **Example**: **OpenAI's fine-tuning guide** shows that with 100 examples, more advanced models perform better; with 550,000 examples, all models perform similarly.

---

## **📌 5. Data Acquisition and Annotation**
The goal of data acquisition is to **gather a diverse dataset** while ensuring **privacy and compliance**.

### **Key Data Sources**
1. **Application Data** → Ideal for relevance and distribution match.
2. **Public Data** → Open-source datasets.
3. **Proprietary Data** → Purchased datasets.
4. **Synthetic Data** → AI-generated data.

📌 **Key Takeaway**: **A "data flywheel" can leverage user-generated data to improve AI models continuously.**

### **Data Annotation Challenges**
- Annotation guidelines must define **what makes a response "good"**.
- Even major AI teams (e.g., LinkedIn) find annotation guidelines **one of the hardest challenges**.

### **Building a Dataset: Step-by-Step Process**
1. Find **existing datasets**.
2. Remove **low-quality** instructions.
3. Filter **low-quality responses**.
4. Manually **write new responses**.
5. **Augment** missing topic areas using **AI-generated synthetic data**.
6. **Manually annotate synthetic data**.

📌 **Key Insight**: **Well-structured annotation guidelines improve both manual and AI-powered annotations**.

---

## **📌 6. Reducing the Need for Large Datasets**
### **Three Strategies for Efficient Data Usage**
1. **Self-supervised → Supervised Learning**  
   - Example: Train on **legal documents** first, then fine-tune on **(question, answer) pairs**.
2. **Less-relevant Data → More Relevant Data**  
   - Example: Train on **tweet sentiment** before fine-tuning on **product sentiment**.
3. **Synthetic Data → Real Data**  
   - Example: Use **AI-generated medical records** before fine-tuning on **real patient data**.

📌 **Key Takeaway**: **Layered fine-tuning approaches can optimize data efficiency.**

---

## **📌 7. Experimenting with Data Size and Diversity**
### **How to Estimate Data Needs**
1. **Start with a small dataset** (~50 examples).
2. **Fine-tune and evaluate improvements**.
3. **Scale up only if necessary**.

📌 **Observation**: **Most models show performance improvements with the first 50-100 fine-tuning examples.**

### **Balancing Budget for Data vs. Compute**
- **Spending more on data** → Less money for compute.
- **Spending more on compute** → Less budget for data collection.

📌 **Key Takeaway**: **The right balance depends on dataset size, fine-tuning method, and base model efficiency.**

---

## **📌 Key Takeaways (3-Sentence Summary)**
1️⃣ **Data curation involves quality, diversity, and quantity, impacting model performance significantly.**  
2️⃣ **A well-mixed dataset is more valuable than a large but unstructured dataset—AI engineering requires careful selection and augmentation of training data.**  
3️⃣ **Optimizing data usage through layering (self-supervised → supervised) and balancing budget constraints is crucial for real-world AI applications.**  

---

# 📌 AI Engineering - Chapter 8.1: Interview Questions & Answers

## **❓ Q1: What is the difference between Data-Centric AI and Model-Centric AI?**
✅ **Answer:**  
- **Model-Centric AI** focuses on improving model performance by **modifying architectures, increasing model size, and optimizing training techniques**.  
- **Data-Centric AI** enhances AI performance by **improving data quality, processing techniques, and dataset diversity** to achieve better results with fewer resources.  
- **Key Insight**: While **both approaches** contribute to AI advancements, **data quality and diversity** are critical for ensuring models generalize well to real-world applications.

📌 **Example**: Meta’s **Llama 3 model** improved performance significantly by **annealing on high-quality code and math data**, demonstrating the power of **data-centric optimization**.

---

## **❓ Q2: How do you determine the right data mix for training an AI model?**
✅ **Answer:**  
1. **Real-world application reflection** → Choose a data mix that matches expected user interactions.  
2. **Experiment-based selection** → Conduct **scaling law experiments** by training small models on different data mixes and extrapolating performance for larger models.  
3. **Coverage and diversity** → Ensure **data captures diverse usage patterns**, which can vary by domain, geography, and linguistic variations.  

📌 **Example**: Meta optimized Llama 3’s training dataset by conducting experiments on **small models**, predicting which data mix would work best for their **large-scale foundation models**.

---

## **❓ Q3: What are the key challenges in data annotation for AI models, and how can they be addressed?**
✅ **Answer:**  
- **Challenge 1**: **Ambiguous labeling criteria** → Without clear guidelines, annotators may label data inconsistently.  
  ✅ **Solution**: Develop **strict annotation rules**, including **examples of good vs. bad labels**.  

- **Challenge 2**: **Ensuring annotation consistency** → Different annotators may have different interpretations.  
  ✅ **Solution**: Conduct **annotator training** and use **AI-assisted labeling tools** for better consistency.  

- **Challenge 3**: **Scalability of manual annotation** → Annotating large datasets manually is time-consuming and expensive.  
  ✅ **Solution**: **Leverage AI-powered annotation tools** (e.g., semi-supervised or synthetic data generation).  

📌 **Example**: **Llama 3 researchers** found that **AI-assisted annotations** were **more reliable** than human-generated ones, particularly for nuanced **safety policies**.

---
