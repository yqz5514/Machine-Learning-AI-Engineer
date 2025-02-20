# AI Engineering - Chapter 1.4 Summary

## 📌 The AI Engineering Stack
AI engineering has evolved **from ML engineering**, leading to a rapidly expanding ecosystem of tools, frameworks, and best practices.  

To build AI applications effectively, we must **understand the AI stack**, which consists of three core layers:  
1. **Application Development**  
2. **Model Development**  
3. **Infrastructure**  

---

## 📌 1. Three Layers of the AI Stack  
| **Layer** | **Description** | **Key Considerations** |
|----------|--------------|----------------|
| **Application Development** | Using foundation models to build AI products. | AI interface, context construction(Prompt engineering), user interfaces, evaluation. |
| **Model Development** | Tools for model training, fine-tuning, and optimizing AI models. | Dataset engineering, inference optimization, pre-training vs. post-training. |
| **Infrastructure** | Managing data and compute, model serving, and monitoring. | Scalability, cost-efficiency, real-time processing. |

📌 **Key Takeaway**: **AI engineers often start at the application layer and move down as needed, whereas ML engineers traditionally focus more on model development.**  

---

## 📌 2. How AI Engineering Differs from ML Engineering  
Although AI and ML engineering share foundational principles, **building AI applications using foundation models differs from traditional ML workflows** in three major ways:  

1️⃣ **Model Adaptation vs. Training**  
- **ML Engineering** → Requires training models from scratch.  
- **AI Engineering** → Uses **pre-trained models**, less on modeling and training, more on model adaption.(e.g. **prompt engineering, fine-tuning, and retrieval-augmented generation (RAG)**.  )

2️⃣ **Computational & Infrastructure Demands**  
- **Foundation models** are significantly larger, requiring **more compute resources** and **low-latency inference optimization**.  
- **AI engineers must be proficient in GPU acceleration, parallelism, and distributed training.**  

3️⃣ **Evaluating Open-Ended Outputs**  
- Traditional ML tasks (e.g., fraud detection) is colse-ended, have **clear ground truths**.  
- AI-generated outputs (e.g., chatbot responses) is open-ended, better for varity tasks but **lack absolute correctness**, making evaluation challenging.  

📌 **Key Takeaway**: **AI engineering prioritizes model adaptation, inference efficiency, and qualitative evaluation, whereas ML engineering focuses on traditional model developmetn, training and evaluation.**  

---

## 📌 2. Model Development: Training, Fine-Tuning & Optimization  
Traditional ML workflows focus on **training models from scratch**, whereas AI engineering primarily involves **adapting pre-trained models**.

### **1️⃣ Training Phases in AI Engineering**
| **Phase** | **Description** | **Compute Requirement** |
|----------|----------------|-----------------|
| **Pre-training** | Training a model from scratch on massive datasets. | **Extremely high (98% of training cost)** |
| **Fine-tuning** | Adjusting a pre-trained model on specific data. | **Moderate** |
| **Post-training** | Further optimizing a model after pre-training (e.g., instruction tuning). | **Varies** |

📌 **Example**:  
- **OpenAI’s InstructGPT** → Pre-training took **98% of compute**, fine-tuning handled **user-specific tasks**.  
- **ChatGPT customization** → Users fine-tune via **context & prompt engineering** instead of direct training.

### **2️⃣ Dataset Engineering**
Traditional ML models rely on **structured tabular data**, whereas AI models work with **unstructured text, images, and videos**.

| **ML Engineering** | **AI Engineering** |
|--------------|-----------------|
| Focuses on **feature engineering** for tabular data. | Focuses on **context retrieval, deduplication, tokenization**. |
| Requires labeled datasets for supervised learning. | Often uses **self-supervised or reinforcement learning**. |

📌 **Key Takeaway**: **AI engineers spend more time on prompt design and retrieval than traditional feature engineering.**  

---

## 📌 3. Inference Optimization & Scalability  
Deploying foundation models requires **careful optimization to balance speed, cost, and scalability**.

### **1️⃣ Challenges in AI Model Deployment**
| **Challenge** | **Why It’s a Problem?** | **Solution** |
|------------|-----------------|------------|
| **Compute Costs** | Foundation models are large, making inference expensive. | Quantization, serverless inference. |
| **Latency Constraints** | Real-time applications need low-latency responses. | Model parallelism, distillation. |
| **Scaling Requests** | Handling thousands to millions of concurrent queries. | Load balancing, autoscaling on cloud. |

### **2️⃣ Key Optimization Techniques**
| **Method** | **Description** | **Example** |
|----------|----------------|-----------|
| **Quantization** | Reducing model precision to lower memory usage. | FP16 → INT8 |
| **Model Distillation** | Training a smaller model to mimic a larger model’s performance. | GPT-3 → GPT-3.5 |
| **Parallel Processing** | Distributing computation across multiple GPUs or clusters. | Tensor Parallelism |

📌 **Key Takeaway**: **AI engineers must optimize inference pipelines to improve efficiency while minimizing costs.**  

---

## 📌 4. AI Application Development & Evaluation 

**The application developmeny layer consists of these responsibilitiesL evaluation, prompt engineering, and AI interface.**

### **1️⃣ Challenges in Evaluating AI Models**
Foundation models introduce **new evaluation challenges** compared to traditional ML models.

| **Challenge** | **Description** |
|-------------|----------------|
| **No Absolute Ground Truth** | Open-ended applications lack a single correct answer. |
| **Contextual Dependence** | Model responses vary significantly based on input phrasing. |
| **Bias & Fairness Issues** | Foundation models may inherit biases from training data. |

### **2️⃣ Evaluation Metrics**
| **Metric** | **Use Case** | **Example** |
|----------|------------|-----------|
| **Perplexity** | Measures model uncertainty in language models. | Lower perplexity = Better fluency. |
| **BLEU / ROUGE** | Evaluates text generation quality. | Summarization & translation models. |
| **Human Preference Score** | Assesses real-world response quality. | RLHF (Reinforcement Learning from Human Feedback). |

📌 **Key Takeaway**: **AI model evaluation requires both automated metrics and human judgment.**  

---

## 📌 5. AI Engineering vs. Full-Stack Engineering  
AI engineering increasingly overlaps with **full-stack development**, as many AI-powered products require **frontend UI integration**.

| **Traditional ML Engineering** | **AI Engineering** |
|------------------|------------------|
| Python-centric, model-focused. | Expanding into JavaScript, Web APIs (e.g., LangChain.js, OpenAI Node SDK). |
| Trained models embedded in backend systems. | AI-powered applications with **user-facing interfaces**. |
| Requires deep ML knowledge. | Web & full-stack developers can build AI applications. |

## 📌 5. AI Engineering vs. Full-Stack Development  
The AI development workflow is increasingly merging with **full-stack engineering**, especially in the **application layer**:  

### **Why Full-Stack Developers are Entering AI Engineering**
- **Pre-trained models make AI accessible to more developers**.  
- **Many AI applications are user-facing, requiring strong UI/UX skills**.  
- **Growing demand for AI-powered web & mobile applications**.  

### **New AI Development Workflow**
| **Traditional ML Workflow** | **AI Engineering Workflow** |
|------------------|------------------|
| Data collection → Model training → Model deployment → Product development | Rapid prototyping → Model selection → Product-market fit → Scaling models & data |


📌 **Key Takeaway**: **The rise of foundation models allows full-stack developers to enter AI engineering, making AI more accessible.**  

---

# 📌 If an Interviewer Asks...

### **❓ Q1: What are the key differences between AI engineering and ML engineering?**  
✅ **Answer:**  
- **ML Engineering** → Focuses on **training models from scratch**, requiring deep ML expertise.  
- **AI Engineering** → Focuses on **adapting pre-trained models**, emphasizing **prompt engineering, fine-tuning, and inference optimization**.  
- **Example**: Fraud detection models are traditionally trained from structured datasets, whereas AI chatbots use **LLMs with prompt engineering & RAG**.

---

### **❓ Q2: What are the major challenges in optimizing inference for large AI models?**  
✅ **Answer:**  
1. **Latency Issues**: Generating responses in real-time is computationally expensive.  
2. **Cost Considerations**: AI inference requires **efficient quantization & load balancing**.  
3. **Scalability Challenges**: AI-powered applications handle millions of queries, demanding **distributed processing**.  

🚀 **Optimization techniques**:  
- **Quantization (FP16 → INT8)** reduces memory footprint.  
- **Distillation** creates smaller, faster models.  
- **Parallelism** enables high-throughput inference.

---

### **❓ Q3: Why is prompt engineering critical in AI application development?**  
✅ **Answer:**  
- **Prompt engineering allows developers to control model behavior without retraining.**  
- **Well-structured prompts significantly improve response quality & consistency.**  
- **Example**: Chain-of-Thought (CoT) prompting enhances AI reasoning abilities.

---

## 📌 Key Takeaways (3-Sentence Summary)  
1️⃣ **AI engineering emphasizes model adaptation, inference optimization, and application development rather than traditional ML training.**  
2️⃣ **Efficient inference and scalable deployment are critical, requiring optimizations like quantization, distillation, and parallel processing.**  
3️⃣ **AI engineering is merging with full-stack development, enabling web & software engineers to build AI-powered applications.**  

---
🔥 **Now this is a complete Markdown summary for GitHub! 🚀**  
📌 **Would you like any modifications or additions? 😊**
