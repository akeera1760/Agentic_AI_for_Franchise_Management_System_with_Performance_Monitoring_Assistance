# 🤖 FranchiseOps AI

## Agentic AI for Franchise Management System with Performance Monitoring Assistance

> **An agentic decision-support copilot for multi-outlet franchise networks — grounded, never fabricated.**

**Codename:** `FranchiseOps AI`
**Program:** Infosys Springboard Internship — Batch 1

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](#)
[![AI Agents](https://img.shields.io/badge/AI-9%20Specialized%20Agents-purple.svg)](#)
[![RAG](https://img.shields.io/badge/RAG-FAISS-green.svg)](#)

---

## 📑 Table of Contents

* [Program & Team Context](#-program--team-context)
* [Project Overview](#-project-overview)
* [Architecture](#-architecture)
* [Specialised AI Agents](#-specialised-ai-agents)
* [Authentication, OTP & Security](#-authentication-otp--security)
* [Admin Dashboard](#-admin-dashboard)
* [Screenshots & Demo](#-screenshots--demo)
* [Installation & Run Instructions](#-installation--run-instructions)
* [Requirements](#-requirements)
* [Environment Variables](#-environment-variables)
* [Known Limitations](#-known-limitations)
* [Future Scope](#-future-scope)
* [Acknowledgements](#-acknowledgements)

---

## 👥 Program & Team Context

### Infosys Springboard Internship — Batch 1

FranchiseOps AI was developed as part of the **Infosys Springboard Internship — Batch 1**, with the objective of building an intelligent franchise-management platform capable of combining business analytics, machine learning, retrieval-augmented generation, and agentic AI.

### Mentor

**Mentor:** `MOHAMEDSIPLI M`
**Designation:** ``

### Team Members

| Name                | Role / What They Built | GitHub        |
| --------------------| ---------------------- | ------------- |
| `Akeeranandan`      |                        | `akeera1760`  |
| `Muskan patel`      |                        |               |
| `Tazreen Rehman`    |                        |               |
| `Venkata Siva Reddy`|                        |               |


---

# 🚀 Project Overview

## Problem Statement

Managing a franchise network involves continuously monitoring outlets, revenue, workforce, inventory, marketing campaigns, customer feedback, audits, and operational documents.

Traditional dashboards can display metrics, but managers still need to manually interpret the information, compare multiple indicators, identify risks, and search through SOPs or compliance documents.

**FranchiseOps AI** addresses this problem by providing an AI-powered decision-support system for franchise owners, regional operations managers, store managers, and staff.

The platform combines structured business data, machine-learning models, visual analytics, specialised AI agents, and document-based RAG to provide grounded operational insights.

## Solution

FranchiseOps AI uses an agentic architecture in which an **AI Copilot routes user questions to specialised business agents**.

Each specialised agent combines:

* SQL-based data aggregation
* Machine-learning model benchmarking
* Business-specific analytics
* Interactive visualisations
* Grounded outputs

For policy and document-based questions, the system can use **FAISS/RAG retrieval** to retrieve relevant information before generating an answer.

The final response is generated using **Qwen2.5-3B-Instruct**, with a **1.5B fallback model** when required.

The system is designed around one core principle:

> **Grounded generation — the AI should answer from retrieved facts rather than fabricate business numbers.**

---

# 🏗️ Architecture

FranchiseOps AI follows a **four-layer architecture**.

```text
┌─────────────────────────────────────────────────────────────┐
│                    4. GENERATION LAYER                     │
│                                                             │
│     Qwen2.5-3B-Instruct → 1.5B fallback                    │
│     Generates grounded final responses                     │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  3. ORCHESTRATION LAYER                    │
│                                                             │
│                    intent_router.py                        │
│                                                             │
│     Question Classification → Agent Routing → Retrieval    │
│                       ↓                                     │
│                    FAISS / RAG                              │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   2. REASONING TOOLS LAYER                 │
│                                                             │
│                 9 Specialized AI Agents                    │
│                                                             │
│ SQL Aggregation + ML Benchmarking + Plotly Visualisation   │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                        1. DATA LAYER                        │
│                                                             │
│                  SQLite Database                            │
│                                                             │
│ Outlets • Staff • Inventory • Marketing • Feedback        │
│                     • Audit Records                         │
└─────────────────────────────────────────────────────────────┘
```

### Architecture Diagram

<img width="907" height="492" alt="image" src="https://github.com/user-attachments/assets/c70e0b46-05be-44e3-957f-778f5ad16588" />


---

# 🧠 Key Differentiators

### 1. Grounded Generation

The AI Copilot retrieves relevant SQL facts and documents before generating responses, reducing the possibility of fabricated business numbers.

### 2. Transparent ML Benchmarking

Instead of relying blindly on one machine-learning algorithm, the specialised agents benchmark multiple models.

The model-performance results can be exposed through the application for transparency.

### 3. Role-Based Access Control

Different users receive different levels of access according to their responsibilities.

### 4. Fail-Soft LLM Architecture

The generation layer supports:

```text
Qwen2.5-3B-Instruct
        ↓
Insufficient VRAM / resource constraint
        ↓
Qwen2.5-1.5B fallback
```

This allows the application to degrade gracefully instead of completely failing.

### 5. Business-Specific AI Agents

Rather than having a single generic chatbot, FranchiseOps AI provides nine specialised agents covering different franchise-management functions.

---

# 🤖 Specialised AI Agents

## Agent Overview

```text
                         AI COPILOT
                     intent_router.py
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
 Workforce             Outlet              Inventory
 & Retention           & Revenue            & Demand
       │                   │                    │
       ├───────────────────┼────────────────────┤
       │                   │                    │
       ▼                   ▼                    ▼
 Marketing             Sentiment             Audit &
   ROI                & Feedback            Compliance
       │                   │                    │
       ├───────────────────┼────────────────────┤
       │                   │                    │
       ▼                   ▼                    ▼
 Executive            SOP Translation       Document RAG
 Digest                NLLB-200              Studio
```

---

## 1. Workforce & Retention Intelligence

**Purpose:** Predicts which employees are at risk of leaving and segments the workforce.

### ML Models Benchmarked

* Random Forest
* Gradient Boosting
* Decision Tree
* Logistic Regression
* Linear Regression
* SVC
* MLP

### Visualisations

* Bar chart
* Box plot
* 3D scatter
* Heatmap

### Output

The agent provides workforce segmentation and employee-retention risk insights.

### Best Model

**Selected model:** `[Insert benchmark winner]`

**Why:** `[Insert reason based on the model-performance ledger, such as highest F1/accuracy or best validated performance.]`

### Data

The overall system's data layer contains staff records. Confirm the exact SQL table names used by the implementation before final submission.

---

## 2. Outlet Intelligence & Revenue Analytics

**Purpose:** Tracks outlet health, revenue drivers, and benchmarks stores against each other.

### ML Models Benchmarked

* Random Forest Regressor
* Gradient Boosting Regressor
* Decision Tree Regressor
* Linear Regression
* SVR

### Visualisations

* Folium map
* Bar chart
* Radar chart

### Output

* Outlet performance
* Revenue analytics
* Store comparison
* Location-based outlet insights


## 3. Inventory Intelligence & Demand Forecasting

**Purpose:** Forecasts SKU demand, identifies stock-out risk, and supports auto-replenishment.

### ML Models Benchmarked

* Random Forest Regressor
* Gradient Boosting Regressor
* Decision Tree Regressor
* Linear Regression
* SVR
* Isolation Forest

### Visualisations

* Treemap
* Line chart
* Funnel
* Heatmap

### Output

* Demand forecasts
* Inventory insights
* Stock-out risk
* Replenishment recommendations


## 4. Marketing ROI Intelligence

**Purpose:** Evaluates campaign ROI, channel effectiveness, and Customer Acquisition Cost.

### ML Models Benchmarked

* Random Forest Regressor
* Gradient Boosting Regressor
* Decision Tree Regressor
* Linear Regression
* SVR

### Visualisations

* Sunburst
* Violin plot
* Bar chart
* Scatter plot

### Output

* Campaign ROI
* Channel effectiveness
* CAC analytics
* Marketing performance insights


## 5. Customer Sentiment & Feedback Analytics

**Purpose:** Performs real-time and batch sentiment analysis across customer feedback with aspect extraction.

### ML Models Benchmarked

* Random Forest Classifier
* Gradient Boosting Classifier
* Decision Tree Classifier
* Logistic Regression
* SVC

### Visualisations

* Density heatmap
* Bar chart
* Line chart

### Output

* Sentiment classification
* Feedback trends
* Aspect-level insights
* Customer feedback analytics


## 6. Audit & Compliance Intelligence

**Purpose:** Predicts audit failure risk, tracks violations, and provides an FSSAI compliance checklist.

### ML Models Benchmarked

* Random Forest Classifier
* Gradient Boosting Classifier
* Decision Tree Classifier
* Logistic Regression
* SVC
* Isolation Forest

### Visualisations

* Sunburst
* Box plot
* Scatter plot

### Output

* Audit risk prediction
* Compliance insights
* Violation tracking
* FSSAI checklist


## 7. Executive Franchise Intelligence Digest

**Purpose:** Generates a one-page rollup of the overall franchise network's health.

Unlike the other analytical agents, this agent uses outputs from **Agents 1–6** rather than maintaining a separate ML benchmark.

### Inputs

* Workforce & Retention
* Outlet & Revenue
* Inventory & Demand
* Marketing ROI
* Customer Sentiment
* Audit & Compliance

### Visualisations

* Gauge / Indicator
* Pie chart
* Bar chart

### Output

An executive-level summary of franchise network health with an AI-generated business digest.

### ML Benchmark

No separate benchmark is required. The agent consumes outputs generated by Agents 1–6.

---

## 8. Multilingual SOP Translation — NLLB-200

**Purpose:** Provides offline translation of text or SOP documents into 20+ languages and supports a franchise business glossary.

### Model

**NLLB-200 distilled-600M**

This is a translation model rather than a classical ML benchmarking task.

### Output

* Multilingual SOP translation
* Business terminology support
* Translated operational documents

### Execution

The translation functionality is designed to operate offline once the required model is available.

---

## 9. PDF SOP & Franchise Agreement RAG Studio

**Purpose:** Provides an upload-your-own-document workbench for SOPs, contracts, and FSSAI guidelines.

Documents are:

```text
PDF / Document
      ↓
Chunking
      ↓
Embedding
      ↓
FAISS Index
      ↓
Semantic Retrieval
      ↓
Grounded Q&A
```

### Retrieval Stack

* FAISS
* Sentence Transformers

### ML Benchmark

No classical ML benchmark is used.

### Output

* Document-based Q&A
* Retrieved supporting information
* Grounded answers from uploaded documents

---

# 🔀 AI Copilot & Intent Routing

The central orchestration component is:

```text
intent_router.py
```

Its responsibilities include:

1. Understanding the user's question.
2. Classifying the question into the appropriate business domain.
3. Routing the question to the relevant specialised agent.
4. Retrieving grounded SQL facts.
5. Using FAISS/RAG for policy and document-related questions.
6. Passing retrieved information to the generation layer.
7. Producing a grounded final response.

### Example

```text
User:
"Which outlets have the highest revenue risk?"

             ↓

Intent Router

             ↓

Outlet & Revenue Agent

             ↓

SQL Data + ML Prediction

             ↓

Visualisation / Metrics

             ↓

LLM Generation

             ↓

Grounded AI Response
```

---

# 🔐 Authentication, OTP & Security

The authentication flow follows:

```text
Signup
   ↓
Login
   ↓
JWT Session
   ↓
Forgot Password
   ↓
OTP Verification
   ↓
Security Question Fallback
   ↓
Password Reset
```

OTP credentials and application secrets are configured through environment variables and are **never committed to the repository**.

---

# 👥 Role-Based Access Control

| Role                                       | Typical Access                                       |
| ------------------------------------------ | ---------------------------------------------------- |
| **Admin**                                  | All tabs, Admin Dashboard and complete agent suite   |
| **Franchise Owner / Regional Ops Manager** | All agents and AI Copilot, excluding Admin Dashboard |
| **Store Manager**                          | AI Copilot + relevant operational agents             |
| **Staff**                                  | AI Copilot + one or two directly relevant agents     |

This role-aware architecture ensures users only access functionality appropriate to their responsibilities.

---

# 🛡️ Admin Dashboard

The Admin Dashboard provides administrative and system-level visibility.

### Admin Capabilities

* User management
* Role assignment
* Database health monitoring
* LLM status monitoring
* Translation-engine status
* ML model performance ledger
* Accuracy / F1 / R² tracking per agent
* Chat history
* Audit trail across users



### 🧰 Technology Stack

---

| Layer           | Technology                  | Purpose                           |
| --------------- | --------------------------- | --------------------------------- |
| Frontend / UI   | Streamlit                   | Interactive application interface |
| Backend         | Python                      | Application and agent logic       |
| Database        | SQLite                      | Structured franchise data         |
| Data Processing | Pandas                      | Data manipulation and analysis    |
| ML              | Scikit-learn                | Model training and benchmarking   |
| Visualisation   | Plotly                      | Interactive charts                |
| Maps            | Folium                      | Geographical outlet visualisation |
| Orchestration   | Python / `intent_router.py` | Query routing                     |
| RAG             | FAISS                       | Vector similarity retrieval       |
| Embeddings      | Sentence Transformers       | Document embeddings               |
| LLM             | Qwen2.5-3B-Instruct         | Response generation               |
| Fallback LLM    | Qwen2.5-1.5B                | Resource-aware fallback           |
| Translation     | NLLB-200                    | Multilingual SOP translation      |
| Authentication  | JWT                         | Session authentication            |
| OTP             | SMTP / Email                | Password-reset verification       |

---

# 📁 Repository Structure

```text
franchiseops-ai/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── docs/
│   ├── architecture-diagram.png
│   ├── screenshots/
│      ├── login.png
│      ├── dashboard.png
│      ├── agent.png
│      ├── copilot.png
│      └── admin-dashboard.png
│   
│   
│      
│
├── milestone-1/
│   └── README.md
│   └── milestone1.ipynb
├── milestone-2/
│   └── milestone2.ipynb
|   └── README.md
├── milestone-3/
|   └── milestone3.ipynb
|   └── README.md

```

---

# ⚙️ Installation & Run Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/<org-or-user>/franchiseops-ai.git
cd franchiseops-ai
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

```bash
cp .env.example .env
```

On Windows, manually create `.env` from `.env.example` if `cp` is unavailable.

Open `.env` and add your own credentials.

**Never commit `.env`.**

## 5. Seed the Database

For the first run:

```bash
python seed_data.py
```

## 6. Start the Application

```bash
streamlit run app.py
```

The Streamlit application should then provide the FranchiseOps AI interface.

---

# ☁️ Run on Google Colab

If the project is also distributed as a Google Colab notebook, add the notebook link here:

**Colab:** `[ADD COLAB LINK]`

### Execution Order

```text
1. Install dependencies
2. Configure secrets
3. Load project files
4. Initialise database
5. Seed database
6. Load ML models
7. Load LLM / fallback model
8. Start application
```

> Replace the above sequence with the exact notebook cell order used by the project.

---

# 💻 Minimum Requirements

The project requires:

* Python 3.x
* Sufficient RAM for application execution
* Additional RAM/VRAM depending on the selected LLM
* Internet access for downloading dependencies and required model weights during setup
* Additional disk space for ML/LLM model files

### LLM Resource Handling

```text
Available resources
       │
       ▼
Qwen2.5-3B-Instruct
       │
       ├── Enough VRAM → Use 3B
       │
       └── Insufficient VRAM
                    ↓
             Use 1.5B fallback
```

### Installation Estimate

> **Expected installation time:** `[ADD ACTUAL TIME AFTER CLEAN INSTALL TEST]`

> **Expected disk space:** `[ADD ACTUAL SIZE INCLUDING MODEL WEIGHTS]`

Large LLM and NLP model weights may require several GB of storage.

---

# 📦 requirements.txt

`requirements.txt` should contain **pinned versions** for all packages used by the codebase.

Example format:

```text
# Core
streamlit==<version>
pandas==<version>
numpy==<version>

# ML
scikit-learn==<version>

# LLM & NLP
torch==<version>
transformers==<version>
bitsandbytes==<version>
sentence-transformers==<version>
faiss-cpu==<version>

# Visualization
plotly==<version>
folium==<version>

# Auth
PyJWT==<version>
python-dotenv==<version>

# Reporting / Document Processing
<package>==<version>
```

> **Important:** Do not copy these placeholders directly into `requirements.txt`. Generate the final file from the successfully tested environment using `pip freeze`, then remove unused packages and organise the resulting pinned dependencies.

### OS-Level Dependencies

Depending on the implementation, additional system dependencies may be required, such as:

* CUDA-compatible drivers
* FFmpeg
* Poppler

Document the exact dependencies required by the final implementation.

---

# 🔑 Environment Variables

Only **variable names** should appear in the repository documentation. Never commit actual credentials.

| Variable                 | Purpose                                     | Where to Get It                                 |
| ------------------------ | ------------------------------------------- | ----------------------------------------------- |
| `HF_TOKEN`               | Hugging Face access token for model weights | Hugging Face account → Settings → Access Tokens |
| `KAGGLE_USERNAME`        | Kaggle API username, if required            | Kaggle account                                  |
| `KAGGLE_KEY`             | Kaggle API credential, if required          | Kaggle → Account → API Token                    |
| `OTP_EMAIL_ADDRESS`      | Dedicated mailbox used for OTP emails       | Project/team Gmail account                      |
| `OTP_EMAIL_APP_PASSWORD` | Gmail App Password used for SMTP            | Google Account → Security → App Passwords       |
| `JWT_SECRET_KEY`         | Secret used for signing JWT sessions        | Generate locally                                |

### Generate JWT Secret

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```




# 🗄️ Data Layer

The data layer is populated by:

```text
seed_data.py
```

and managed through:

```text
db.py
```

The project documentation identifies the following major data domains:

* Outlets
* Staff
* Inventory
* Marketing
* Customer Feedback
* Audit Records

The database is implemented using SQLite according to the project architecture.

---

# 🔍 Grounded RAG Pipeline

The Document RAG Studio provides grounded answers from uploaded business documents.

```text
                Upload Document
                       │
                       ▼
                Extract Content
                       │
                       ▼
                   Chunking
                       │
                       ▼
              Sentence Transformer
                   Embeddings
                       │
                       ▼
                 FAISS Index
                       │
                       ▼
               Similarity Search
                       │
                       ▼
              Relevant Context
                       │
                       ▼
                 LLM Generation
                       │
                       ▼
               Grounded Answer
```

Supported use cases include:

* SOP question answering
* Franchise agreement queries
* FSSAI guideline queries
* Internal operational documentation
* Uploaded PDF knowledge bases

---

# 🌐 Multilingual SOP Translation

The translation agent uses:

**NLLB-200 distilled-600M**

It supports offline translation of text and SOP documents into **20+ languages**, together with a franchise-business glossary.

```text
English SOP
     │
     ▼
NLLB-200
     │
     ├── Language 1
     ├── Language 2
     ├── Language 3
     └── ...
```

---

# 📈 Visual Analytics

FranchiseOps AI uses interactive visualisations to make analytical outputs easier to understand.

| Agent            | Visualisations                     |
| ---------------- | ---------------------------------- |
| Workforce        | Bar, Box Plot, 3D Scatter, Heatmap |
| Outlet           | Folium Map, Bar, Radar             |
| Inventory        | Treemap, Line, Funnel, Heatmap     |
| Marketing        | Sunburst, Violin, Bar, Scatter     |
| Sentiment        | Density Heatmap, Bar, Line         |
| Compliance       | Sunburst, Box Plot, Scatter        |
| Executive Digest | Gauge / Indicator, Pie, Bar        |

---

# ⚠️ Known Limitations

The following limitations should be stated honestly according to the actual implementation:

1. **Synthetic / seeded data:** The project may rely on seeded or synthetic franchise data rather than live enterprise data.
2. **SQLite database:** SQLite is suitable for development and demonstration but may require migration to a production database for large-scale deployments.
3. **Single-tenant architecture:** The current implementation may require additional work for true multi-tenant franchise organisations.
4. **Local model resources:** Running the larger LLM locally can require substantial RAM/VRAM and disk space.

> Update these points if the final implementation differs.

---

# 🔮 Future Scope

Potential improvements include:

1. **Production database integration**
   Replace SQLite with PostgreSQL or another scalable production database.

2. **Enterprise multi-tenancy**
   Support multiple franchise organisations with isolated data and permissions.

3. **Real-time business integrations**
   Connect POS, ERP, inventory, HR, CRM, and marketing platforms.

4. **Advanced predictive analytics**
   Introduce continuously retrained models using real operational data.

5. **Cloud deployment**
   Deploy the AI agents and LLM infrastructure using scalable cloud services.

6. **Advanced agent orchestration**
   Allow multiple specialised agents to collaborate on complex business questions.

7. **Mobile support**
   Provide franchise owners and store managers with mobile-first operational access.

---

# 🙏 Acknowledgements

This project was developed as part of the:

**Infosys Springboard Internship — Batch 1**

We sincerely thank MOHAMEDSIPLI M, **[Designation]**, for the guidance and support provided throughout the project.

We also acknowledge the Infosys Springboard team for providing the learning and development opportunity.

---


---

## 🏁 FranchiseOps AI

> **From raw franchise data to grounded decisions — one intelligent copilot for the entire franchise network.**

**Infosys Springboard Internship — Batch 1**
