---

## AI & ML Engineering knowledge Tree (to be updated weekly)

```text

├── 1️⃣ ML System Design （机器学习系统设计）
│   │
│   ├──what is ML?
│   │   ├──machine can learn the complex patttern from exist data, 
│   │   │   and use that pattern to make prediction on unseen data
│   │
│   ├──what are ML suit for(or good at)?
│   │   ├──capability of learning(if no pattern exist, no need for ML)
│   │   ├──complex pattern 
│   │   ├──Existing Data (data is avaliable or it's possible to collect)
│   │   ├──Prediction (t’s a predictive problem, estimated values.)
│   │   ├──unsenn data (share similar distribution with exist data)
│   │   ├──more details 
│   │   │   ├──the cost of wrong prediction is cheap (need trade off)
│   │   │   ├──repetitive
│   │   │   ├──at scale
│   │   │   ├──patterns are constantly changing
│   │
│   ├──When do not use ML?
│   │   ├──ML 解决方案不符合伦理道德（例如 AI 招聘系统可能带有偏见）。
│   │   ├──更简单的传统方法足够（不需要复杂的 ML 方案）。
│   │   ├──问题可以拆分 → 例如，不能构建一个全自动 AI 客服，但可以用 ML 预测用户是否FAQ 里找到答案，然后引导他们联系人工客服。
│   │
│   ├── Research vs Production（Research vs Production）
│   │   ├── Goal：SOTA&high performance VS business metrics driven,balancing speed, interpretability, and cost
│   │   ├── Data：Static Vs onstantly changing,bias,unstrutued
│   │   ├── Computational Priority：Throughput vs Latency
│   │   ├── Fairness & Bias: not focus vs Must
│   │   ├── Interpretability: not focus vs Must
│   │   ├── 真实案例：Netflix 推荐系统优化
│   │
│   ├── 机器学习系统流程框架(ch2)
│   │   ├── Business objectives (Aligning ML Metrics with Business Goals)
│   │   ├── Data stack（Data Pipeline）
│   │   ├── Infrastructure
│   │   ├── Deployment
│   │   ├── Monitoring & Feedback Loop）
│   │
│   ├── Framing ML problems (ch2)
│   │   ├── Input 
│   │   ├── Output -- output type dictates task type of ML problem (classification, regression)
│   │   ├── Objective/loss function
│   │
│   ├── The Iterative ML Development Process(cyclical) (ch2)
│   │   ├── Project Scoping
│   │   ├── Data Engineering
│   │   ├── ML Model Development
│   │   ├── Deployment
│   │   ├── Monitoring & Continuous Learning
│   │   ├── Business Impact Analysis
│   │
│   ├── ML System core system requirments(ch2):
│   │   ├── Reliability (strong monitoring, human in the loop sys)
│   │   ├── Scalability
│   │   ├── Maintainability
│   │   ├── Adaptability
│   │
│   ├── 机器学习模型的可维护性（Maintainability）
│   │   ├── 模型版本管理（Model Versioning）
│   │   ├── 可解释性（Interpretability & Explainability
│   │   ├── 监管 & 合规（Regulatory Compliance）
│   │
│   ├── 机器学习系统优化(ch1.2)
│   │   ├── 低延迟推理（Latency Optimization）（what is latency?how to analyze and measure?每个方法的优缺点？适用场景？）
│   │   │   ├── Batch Processing（批量推理）-- commonly used in  large distributed ML system
│   │   │   ├── Quantization（模型量化）
│   │   │   ├── Distillation（模型蒸馏）
│   │   │   ├── Caching Strategies（缓存策略）
│   │   ├── 高吞吐量优化（Throughput Optimization）(what is throughout? how to analyze and measure)
│   │   │   ├── 并行推理（Parallel Inference）
│   │   │   ├── Load Balancing（负载均衡）
│   │   ├── 真实案例：Google 语音助手的低延迟优化
│   │   │ 
│   │   ├──系统优化 Trade-off（权衡优化）
│   │   │   ├── 计算效率 vs 预测精度（Performance vs Accuracy）
│   │   │   ├── 低延迟 vs 高吞吐量（Latency vs Throughput）
│   │   │   ├── 资源消耗 vs 可扩展性（Cost vs Scalability）
│   │   │   ├── 真实案例：推荐系统如何在精准度 & 计算成本之间做取舍？
│   │
├── 2️⃣ AI Engineering（AI 工程）
│   ├── 传统 ML vs AI Engineering
│   │   ├── 传统 ML 关注模型训练（Train from Scratch）
│   │   ├── AI Engineering 关注模型适配（Adapt Pre-trained Models）
│   │   ├── AI 开发者技能：Prompt Engineering, RAG, Fine-Tuning
│   │
│   ├── AI 开发三大层次 （ch1.4）
│   │   ├── 应用层（Application Layer）
│   │   │   ├── LLM API 开发（LangChain, OpenAI API）
│   │   │   ├── AI 应用（AI Chatbot, 智能搜索, 生成式 AI）
│   │   │   ├── Prompt Engineering（提示工程
│   │   │   ├── Evaluating AI Models
│   │   ├── 模型层（Model Development Layer）
│   │   │   ├── Dataset engineering 
│   │   │   ├── Fine-Tuning（微调 & LoRA）& optimization
│   │   │   ├── pre-training vs post-training
│   │   │   ├── Retrieval-Augmented Generation（RAG）
│   │   │   ├── Inference Optimization & Scalability
│   │   ├── 基础设施层（Infrastructure Layer）
│   │   │   ├── MLOps（MLflow, Weights & Biases）
│   │   │   ├── 部署优化（Kubernetes, TensorRT, ONNX）
│   │   │   ├── AI 监控（Evidently AI, Drift Detection）
│   │
│   ├── LLM 生态系统
│   │   ├── LLM vs Foundation Models
│   │   ├── 主要 LLM 提供商（OpenAI, Google, Anthropic）
│   │   ├── LLM 适配技术（Prompt Engineering vs Fine-Tuning）
│   │   ├── 企业 LLM 选型：API vs 自研模型
│   │
│   ├── AI 生产环境中的优化策略
│   │   ├── 部署优化（Deploying LLMs at Scale）
│   │   │   ├── Serverless vs GPU Deployment
│   │   │   ├── API Gateway 设计
│   │   ├── 成本优化（Cost Optimization）
│   │   │   ├── Token Usage Reduction
│   │   │   ├── Edge AI & On-Device Models
│   │
│   ├── AI 真实应用案例（Industry Applications）
│   │   ├── AI 搜索引擎（Google Search + RAG）
│   │   ├── AI 辅助编程（GitHub Copilot, ChatGPT Code Interpreter）
│   │   ├── AI 个性化推荐（Netflix, Spotify, TikTok）
│   │   ├── AI 医疗（AI 影像分析, 疾病预测）
│   │   ├── AI 生成式设计（Midjourney, Adobe Firefly）
│   ├── AI 应用落地案例
│   │   ├── 推荐系统（YouTube, TikTok）
│   │   ├── AI 搜索（Google, Bing, Perplexity AI）
│   │   ├── AI 写作工具（ChatGPT, Jasper, Grammarly）
│
├── 3️⃣ MLOps（机器学习运维）
│   ├── MLOps 生命周期（MLOps Lifecycle）
│   │   ├── 数据版本管理（DVC, Feature Store）
│   │   ├── 模型监控（Evidently AI, Prometheus）
│   │   ├── 模型 CI/CD（MLflow, Vertex AI, AWS SageMaker）
│   │
│   ├── MLOps 优化策略
│   │   ├── 灰度发布 & A/B 测试
│   │   ├── 自动化数据标注 & 训练
│   │   ├── 迁移学习（Transfer Learning in Production）
│   │
│   ├── 真实案例
│   │   ├── 如何优化 Google Search AI 生产环境
│   │   ├── Facebook 计算广告 AI Pipeline
│
└── 4️⃣ AI & ML 面试准备
    ├── 机器学习系统设计（ML System Design Interviews）
    │   ├── AI 生产环境架构设计
    │   ├── 模型部署优化（LLM API, Vector Search）
    │   ├── 数据管道设计（Data Pipelines）
    ├── AI 工程师面试技巧（AI Engineering Interviews）
    │   ├── 代码面试（LeetCode, System Design）
    │   ├── LLM 相关问题（Prompt Engineering, RAG）
    │   ├── AI 生产落地问题（如何优化 AI 应用的延迟？）

# 📌 Knowledge Tree: Machine Learning System - Data Engineering Fundamentals (Designing Machine Learning Systems - Chapter 3)

├── 1️⃣ Data Sources & Data Formats
│   ├── User Input Data (Text, Images, Logs)
│   ├── System-Generated Data (Model Predictions, Event Logs)
│   ├── Internal Databases (Enterprise CRM, Inventory)
│   ├── Third-Party Data (Paid, Open Source)
│   ├── Structured Formats (JSON, CSV, Parquet)
│   ├── Row-major vs. Column-major Storage
│
├── 2️⃣ Data Models & Storage
│   ├── Relational Databases (SQL, PostgreSQL, MySQL)
│   ├── Document Databases (NoSQL, MongoDB)
│   ├── Graph Databases (Neo4j, Amazon Neptune)
│   ├── OLTP (Transactional) vs. OLAP (Analytical)
│
├── 3️⃣ Data Storage Engines & Processing
│   ├── Data Warehouses (BigQuery, Snowflake)
│   ├── Data Lakes (S3, HDFS)
│   ├── Hybrid Storage: Lakehouses (Databricks, Apache Iceberg)
│   ├── ETL (Extract, Transform, Load)
│   ├── ELT (Extract, Load, Transform)
│   ├── Batch Processing (Apache Spark, MapReduce)
│   ├── Stream Processing (Apache Flink, Kafka Streams)
│
├── 4️⃣ Dataflow & Communication
│   ├── Database-Based Communication (Shared Databases)
│   ├── API-Based Services (REST, RPC)
│   ├── Event-Driven Messaging (Kafka, Pub/Sub)
│
├── 5️⃣ Data Curation & Deduplication
│   ├── Data Labeling & Feature Engineering
│   ├── Removing Duplicate Data (MinHash, Bloom Filters)
│   ├── Data Quality Control (Consistency, Relevance, Compliance)
│
├── 6️⃣ Data Transformation & Feature Engineering
│   ├── Feature Extraction (Scaling, Normalization)
│   ├── Data Pruning (Selecting Most Valuable Features)
│   ├── Data Augmentation for Robustness
│
└── 7️⃣ Data Computation & ML Pipelines
    ├── Optimizing SQL Queries for ML Pipelines
    ├── Distributed Data Processing (Dask, Spark)
    ├── Data Partitioning Strategies (Sharding, Indexing)
    ├── Model Training & Serving Pipelines
    ├── ML System Monitoring & Data Drift Detection

📌 **Key Insight**: **ML systems require structured, high-quality datasets, efficient batch processing, and robust data storage models to train high-performance models.**

# 📌 Knowledge Tree: AI Engineering-Dataset Engineering (AI Engineering - Chapter 8)

├── 1️⃣ Data Collection & Sources
│   ├── First-Party Data (User Interaction, Logs)
│   ├── Public & Proprietary Data (Licensed Datasets)
│   ├── AI-Generated Synthetic Data
│
├── 2️⃣ Data Curation & Preprocessing
│   ├── Defining Desired AI Model Behaviors
│   ├── Data Cleaning (Removing Bias, Ensuring Consistency)
│   ├── Filtering Low-Quality Data (Data Pruning)
│   ├── Formatting Data (Tokenization, Instruction-Response Pairs)
│
├── 3️⃣ Data Augmentation & Synthesis
│   ├── Traditional Data Augmentation (Image Rotation, Text Paraphrasing)
│   ├── AI-Synthesized Data (Self-Supervised Learning)
│   ├── Preference Data (Human Preference Fine-Tuning)
│   ├── Chain-of-Thought (CoT) Annotation for Reasoning
│
├── 4️⃣ Data Storage & Processing Pipelines
│   ├── Data Lakes (S3, Delta Lake)
│   ├── Real-Time Data Warehouses (BigQuery, Snowflake)
│   ├── Event-Driven Storage (Kafka, Kinesis)
│   ├── ELT Pipelines (Faster Data Loading, Flexible Queries)
│
├── 5️⃣ AI-Specific Data Engineering
│   ├── Instruction Fine-Tuning Data (GPT, Llama)
│   ├── Self-Supervised Pretraining Data
│   ├── RLHF (Reinforcement Learning from Human Feedback)
│   ├── AI-Assisted Annotation (LLM-Powered Labeling)
│
├── 6️⃣ Data Pipelines for AI Applications
│   ├── API-Based Data Retrieval (REST, GraphQL)
│   ├── Streaming Data Processing (Apache Flink, Spark Streaming)
│   ├── Microservice Architectures for AI Deployment
│
├── 7️⃣ Scaling AI Data Pipelines
│   ├── Model Distillation (Transferring Knowledge from Large Models)
│   ├── Reducing Model Serving Costs with Quantization
│   ├── Optimizing Data Fetching for Low-Latency AI Applications
│
└── 8️⃣ Future of AI Data Engineering
    ├── Real-Time Model Updating via AI-Synthesized Data
    ├── AI-Powered Data Curation & Filtering
    ├── Ethical AI & Compliance in Data Processing
    ├── Addressing Model Collapse in AI Training

📌 **Key Insight**: **AI Engineering focuses on scalable, real-time data pipelines, leveraging AI-synthesized data and self-supervised learning to create adaptable AI models.**


```
