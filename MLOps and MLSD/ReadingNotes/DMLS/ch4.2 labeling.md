# 📌 Designing Machine Learning Systems - Chapter 4.2: Labeling

## **📌 The Role of Labeling in ML Systems**
- **High-quality labeled data** is essential for **training supervised ML models**.
- **Challenges in obtaining labeled data**:
  - **Costly**: Requires human annotation, especially for expert domains.
  - **Privacy Concerns**: Sensitive data cannot be easily outsourced for labeling.
  - **Slow Process**: Manual labeling takes time, affecting iteration speed.

📌 **Key Takeaway**: **Labeling is expensive and slow, but alternative approaches (e.g., weak supervision, semi-supervision, active learning) help mitigate challenges.**

---

## **📌 4.2.1 Hand Labeling**
### **🚨 Challenges of Hand Labeling**
1. **Expensive**:  
   - Requires **domain experts** (e.g., radiologists for medical imaging).
   - Expert time is **limited and costly**.
2. **Privacy Issues**:  
   - **Medical records, financial data** cannot be sent to third-party labelers.
   - **Data security regulations** (e.g., HIPAA, GDPR) limit outsourcing.
3. **Slow Process**:  
   - Speech transcription takes **400x longer** than the actual utterance duration.
   - **Slow labeling → slow model iteration** → poor adaptability.

📌 **Key Takeaway**: **Hand labeling is high-quality but expensive, slow, and privacy-sensitive.**

---

## **📌 4.2.1.1 Label Multiplicity**
- **Different annotators have different accuracy levels**, leading to **conflicting labels**.
- **Higher domain expertise → More annotator disagreements**.
- **Solution**:  
  - **Clear problem definitions** for annotators.
  - **Standardized annotation guidelines**.
  - **Consensus mechanisms (majority vote, adjudication by experts).**

📌 **Example**:  
- **Medical diagnosis labeling** often has **conflicting opinions** among doctors.
- **Crowdsourced labeling** (e.g., Amazon Mechanical Turk) has **lower accuracy**.

---

## **📌 4.2.1.2 Data Lineage**
- **Tracking the origin of labeled data** is crucial for **debugging ML models**.
- **Problem Example**:  
  - **New data is added** from a lower-quality source.
  - **Model performance degrades** due to noisy labels.
- **Solution**:  
  - Maintain **metadata** about data sources, annotators, and confidence scores.
  - Use **data lineage tracking** to **debug model failures**.

📌 **Key Takeaway**: **Keeping track of data sources helps ensure label quality and detect potential biases.**

---

## **📌 4.2.2 Natural Labels**
- **Natural labels** are generated from real-world outcomes **without human intervention**.
- **Example Tasks**:
  - **ETA prediction (Google Maps)**: The actual travel time acts as the ground truth.
  - **Stock price forecasting**: Future prices validate past predictions.
  - **Recommendation systems**:
    - **Behavioral Labels**: A **click, like, purchase** acts as implicit feedback.
    - **Explicit Labels**: Users **rate or review** recommendations.

📌 **Key Takeaway**: **Natural labels reduce annotation costs but require careful handling of feedback biases.**

---

## **📌 4.2.2.1 Feedback Loop Length**
- **Feedback loop length** = Time between model prediction and obtaining ground truth.
- **Short feedback loops**:
  - Click predictions (**minutes**).
  - Social media recommendations (**real-time**).
- **Long feedback loops**:
  - Clothing recommendations (**weeks** until user feedback).
  - Fraud detection (**months** until fraudulent transactions are discovered).

📌 **Trade-off**:
- **Short loops → Faster model iteration** but risk of **premature labeling**.
- **Long loops → Higher accuracy** but **slower adaptability**.

---

## **📌 4.2.3 Handling the Lack of Labels**
Because **labeling is expensive**, alternative methods are used:

| **Method** | **Description** | **Use Case** | **Ground truths required?** |
|-----------|---------------|-------------|-------------|
| **Weak Supervision** | Uses heuristics/rules(often nosiy) to generate labels. | Medical NLP with expert-defined keywords. |No, but a small number of labels are recommended to guide the development of heuristics|
| **Semi-Supervised Learning** | Uses a small labeled dataset to generate more labels. structural assumptions to generate labels | Image classification with limited annotations. |Yes, a small number of initial labels as seeds to generate more labels|
| **Transfer Learning** | Uses models pretrained on another task for your new task. | Fine-tuning BERT for domain-specific NLP. |No for zero-shot learning. Yes for fine-tuning, though the number of ground truths required is often much smaller than what would be needed if you train the model from scratch|
| **Active Learning** | Labels data Yes samples that are most useful to your model. | Prioritizing edge cases in fraud detection. | Yes|

---

## **📌 4.2.3.1 Weak Supervision**
- **Uses heuristics to label data, labeling function (LF): a function that encodes heuristics.** (e.g., keyword matching, rule-based logic).
- **Open Source Weak Supervision Tool**: Snorkel (Stanford AI Lab).
- **Example**:
  - **Medical triage**: If a nurse's note mentions "pneumonia," classify as **urgent**.
  - **Legal NLP**: If a contract contains "termination clause," label as **high-risk**.

📌 **Challenges**:
- **Labels are noisy**.
- **Heuristics may not generalize well**.
- **Solution**: Combine multiple heuristics and refine using **a small set of hand-labeled data**.

**Compare with hand labeling**
- Cost saving: Expertise can be versioned, shared, and reused across an organization
- Privacy: Create LFs using a cleared data subsample and then apply LFs to other data without looking at individual samples
- Fast: Easily scale from 1K to 1M samples
- Adaptive: When changes happen, Every change just reapply LFs!

---

## **📌 4.2.3.2 Semi-Supervision**
- Uses **a small labeled dataset** to infer labels for **unlabeled data**.


**Classic Method**: **Self-training**:
  1. Train on **labeled data**.
  2. Predict labels for **unlabeled data**.
  3. Add **high-confidence predictions** to labeled set.
  4. Retrain until performance plateaus.

**Variants**:
- **Similarity-based**: If two data points have similar features, they share a label.
- **Perturbation-based**: Slight changes to a sample shouldn’t alter the label.

**Considerations**:
- Balancing **limited labeled data** between **training** and **evaluation**.
- **Risk**: Overfitting if the same small set is used repeatedly for model selection.

📌 **Example**:
- **KNN-based Semi-Supervision**:  
  - If **two documents have similar embeddings**, assign the same label.
- **Perturbation-Based Semi-Supervision**:  
  - Small variations in an image shouldn’t change its label.

---

## **📌 4.2.3.3 Transfer Learning**
- **Uses a pretrained model as a starting point** for new tasks.
- **Two types**:
  - **Zero-shot learning**: Directly using the pretrained model.
  - **Fine-tuning**: Further training the model on domain-specific data.

📌 **Examples**:
- **BERT → Sentiment Analysis** (fine-tuned on customer reviews).
- **YOLO → Custom Object Detection** (fine-tuned on company-specific images).

### **Benefits**:
- **Less labeled data** needed for new tasks.
- **Significant performance boost** over training from scratch.
- **Enables** tasks otherwise impossible (e.g., specialized image or language tasks).


📌 **Trend**: **Bigger pretrained models** (e.g., GPT, BERT) → **Better downstream performance**.

---

## **📌 4.2.3.4 Active Learning**
- **The model selects which samples to label** to maximize learning efficiency.

📌 **Example**:
- **Self-driving cars**:
  - Prioritize labeling **rare edge cases** (e.g., pedestrians crossing unexpectedly).

- **Heuristic Approaches**:
  1. **Uncertainty Sampling**: Label most **uncertain** predictions.
  2. **Query-by-Committee**: Multiple models disagree → prioritize labeling that sample.
  3. **Gradient-Based**: Select samples that **most significantly impact** model weights.

**Data Sources**:
- **Synthesized**: Model generates samples in the input space it’s uncertain about.
- **Pool-Based**: Choose from a **large unlabeled dataset**.
- **Online/Production**: Model picks uncertain samples **in real-time** from incoming data.

📌 **Key Benefit**: **Fewer labels needed** while still achieving **high accuracy**—especially valuable with **expensive domain experts**. 
                    **Reduces labeling cost while improving model performance.**

---

## **📌 Final Takeaways (3-Sentence Summary)**
1️⃣ **Hand labeling is expensive, slow, and limited by privacy concerns, but alternative techniques (natural labels, weak supervision, transfer learning) help scale data labeling.**  
2️⃣ **Feedback loops determine how quickly models can improve, with shorter feedback loops enabling faster iteration but increasing premature labels.**  
3️⃣ **Active learning and semi-supervision allow models to intelligently select or generate labels, reducing the need for large-scale manual annotation.**  
1️⃣ **Hand labeling provides high-quality data but is expensive, slow, and poses privacy risks.**  
2️⃣ **Many tasks rely on natural labels (feedback from user behavior), but feedback loop length and potential biases must be managed.**  
3️⃣ **When labeling resources are limited, techniques like weak supervision, semi-supervision, transfer learning, and active learning help reduce costs and improve model performance.**  

---
## **📌 Interview Questions & Answers: Labeling in Machine Learning Systems**

### **❓ Q1: What are the main challenges of manual labeling in machine learning, and how can they be mitigated?**
✅ **Answer:**  
- **Challenges of Manual Labeling**:
  1. **High cost** → Requires human experts (e.g., radiologists for medical images).
  2. **Privacy concerns** → Sensitive data (e.g., medical, legal) cannot be outsourced.
  3. **Time-consuming** → Labeling large datasets delays model iteration.

- **Mitigation Strategies**:
  1. **Weak supervision** → Use heuristics and rules to generate noisy labels.
  2. **Semi-supervised learning** → Use a small labeled dataset to label more data.
  3. **Active learning** → Prioritize labeling the most informative samples.

📌 **Example**:  
- **Self-driving car datasets** often use **active learning** to prioritize labeling **edge cases** (e.g., pedestrians crossing outside crosswalks).

---

### **❓ Q2: What are natural labels, and what are the risks associated with using them?**
✅ **Answer:**  
- **Definition**: Natural labels are derived from real-world user behavior instead of manual annotation.  
- **Examples**:
  - **Search ranking**: If a user clicks on a link, it’s labeled as relevant.
  - **Recommendation systems**: Purchases, likes, or shares act as implicit labels.
  - **ETA predictions**: The actual travel time serves as a label for model evaluation.

- **Risks of Using Natural Labels**:
  1. **Feedback loop bias** → Models reinforce past recommendations (e.g., filter bubbles).
  2. **Delayed feedback** → Some labels take weeks/months to materialize (e.g., fraud detection).
  3. **Noisy labels** → User actions may not always indicate correctness.

📌 **Example**:  
- A **news recommendation system** using clicks as labels may **prioritize clickbait headlines** over high-quality journalism.

---

### **❓ Q3: How does active learning reduce labeling costs, and what are its key selection strategies?**
✅ **Answer:**  
- **Goal**: Reduce the amount of labeled data needed by selecting **only the most informative samples**.
- **How It Works**:
  1. The model **identifies uncertain samples**.
  2. A human annotator **labels only those samples**.
  3. The model retrains on the updated dataset.

- **Key Selection Strategies**:
  1. **Uncertainty Sampling** → Label samples where the model is least confident.
  2. **Query-by-Committee** → Label samples where multiple models disagree.
  3. **Gradient-Based Selection** → Label samples that would cause **the highest model updates**.

📌 **Example**:  
- **Medical AI applications** use **active learning** to prioritize labeling **rare, high-uncertainty cases**, reducing annotation costs.

---

