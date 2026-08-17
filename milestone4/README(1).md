# 🚀 FranchiseOps AI — Aurora Command

> An AI-powered franchise operations platform with predictive analytics, conversational intelligence, document RAG, multilingual translation, anomaly detection, and operational simulation.

## 📌 Overview

**FranchiseOps AI — Aurora Command** is a Streamlit-based intelligent operations platform generated and launched from the `FranchiseOps_AI_Aurora_Redesign_FIXED.ipynb` notebook.

The system combines structured franchise data, machine-learning models, an AI Copilot, document retrieval, multilingual translation, operational alerts, and interactive visual analytics in one interface.

The notebook creates the complete application inside the `franchise_app/` directory.

---

## ✨ Main Capabilities

- 🤖 AI Copilot
- 👥 Workforce intelligence
- 🏬 Outlet and revenue analytics
- 📦 Inventory intelligence
- 📈 Marketing analytics
- 💬 Customer sentiment analysis
- 📋 Audit and compliance analytics
- 📧 Executive intelligence digest
- 🌐 Multilingual SOP translation
- 📄 PDF RAG Studio
- 🔔 Operational notifications
- 🕸️ Knowledge Graph
- ⚡ Digital Twin simulation
- 🚨 Anomaly Scanner
- 📡 Data Feed Center
- 🛡️ Admin Dashboard
- 🧑 User profile and security settings
- 🔐 Authentication, OTP and role-based access

---

# 🧠 AI Copilot

The AI Copilot is the central conversational interface.

A user can ask questions about different parts of the operational database. The intent router detects one or more relevant domains and builds a grounded context before sending the request to the language model.

### Processing flow

```text
User Question
      ↓
Intent Detection
      ↓
Relevant Database Queries
      ↓
RAG Retrieval (when applicable)
      ↓
Grounded Context
      ↓
Qwen 2.5
      ↓
Final Answer
```

The router can work across multiple domains, allowing a question to combine information from different operational areas.

---

# 🤖 Intelligence Agents

## 1. Workforce Intelligence

Analyzes the staff roster and employee-related operational indicators.

### Capabilities

- Attrition-risk analysis
- Employee segmentation
- Workforce statistics
- Staff performance insights

### Models

- Random Forest
- Gradient Boosting
- Decision Tree
- Logistic Regression
- Linear Regression
- SVC
- MLP

### Charts

- Bar charts
- Box plots
- 3D scatter plots
- Heatmaps

---

## 2. Outlet Intelligence

Provides outlet-level performance and revenue analytics.

### Capabilities

- Outlet performance comparison
- Revenue analysis
- Revenue forecasting
- Outlet health indicators
- Geographic analysis

### Models

- Random Forest Regressor
- Gradient Boosting Regressor
- Decision Tree Regressor
- Linear Regression
- SVR

### Charts

- Folium maps
- Bar charts
- Radar charts

---

## 3. Inventory Intelligence

Analyzes stock levels and demand-related indicators.

### Capabilities

- Demand analysis
- Stock-out risk
- Reorder analysis
- Inventory monitoring
- Inventory anomaly detection

### Models

- Random Forest Regressor
- Gradient Boosting Regressor
- Decision Tree Regressor
- Linear Regression
- SVR
- Isolation Forest

### Charts

- Treemaps
- Line charts
- Funnels
- Heatmaps

---

## 4. Marketing Intelligence

Analyzes franchise marketing campaigns and their performance.

### Capabilities

- Campaign analysis
- Marketing ROI
- Channel performance
- Budget analysis
- Conversion analysis

### Models

- Random Forest Regressor
- Gradient Boosting Regressor
- Decision Tree Regressor
- Linear Regression
- SVR

### Charts

- Sunburst
- Violin plots
- Bar charts
- Scatter plots

---

## 5. Customer Sentiment Intelligence

Analyzes customer feedback and sentiment.

### Capabilities

- Sentiment classification
- Customer feedback analysis
- Rating analysis
- Feedback trends
- Aspect-level analysis

### Models

- Random Forest Classifier
- Gradient Boosting Classifier
- Decision Tree Classifier
- Logistic Regression
- SVC

### Charts

- Density heatmaps
- Bar charts
- Line charts

---

## 6. Audit Intelligence

Provides franchise audit and compliance analysis.

### Capabilities

- Audit-risk prediction
- Violation analysis
- Compliance monitoring
- FSSAI-related checklist
- Anomaly detection

### Models

- Random Forest Classifier
- Gradient Boosting Classifier
- Decision Tree Classifier
- Logistic Regression
- SVC
- Isolation Forest

### Charts

- Sunburst
- Box plots
- Scatter plots

---

## 7. Executive Digest

Creates a high-level summary of the franchise network.

The digest combines operational insights and generates an executive-friendly view.

### Charts

- Gauge / Indicator
- Pie charts
- Bar charts

---

## 8. Multilingual Translation

The translation module provides multilingual SOP and text translation.

### Primary Model

```text
facebook/nllb-200-distilled-600M
```

The application includes mappings for multiple languages, including:

- English
- Hindi
- Telugu
- Tamil
- Kannada
- Malayalam
- Marathi
- Bengali
- Gujarati
- Punjabi
- Urdu
- Nepali
- Sinhala
- French
- German
- Spanish
- Chinese
- Japanese
- Arabic
- and others

### Translation flow

```text
Input Text
    ↓
NLLB-200
    ↓
Local Translation Backend
    ↓
Fallback Translator
    ↓
Translated Text
```

---

## 9. PDF RAG Studio

The PDF RAG Studio allows users to ask questions about uploaded documents.

### Workflow

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding
 ↓
FAISS + BM25
 ↓
Relevant Chunks
 ↓
Grounded Answer
```

The RAG engine uses hybrid dense and sparse retrieval.

### Retrieval components

- FAISS
- BM25
- Sentence Transformers
- PDF text extraction

The system can use a franchise knowledge base and uploaded PDF documents.

---

# 🔔 Operational Modules

## Notifications

Displays operational alerts generated from franchise and logistics data.

Alerts can include categories such as:

- Customs Hold
- Typhoon Storm
- Port Congestion
- Vessel Mechanical
- Bunker Fuel Surcharge

---

## 🕸️ Knowledge Graph

The Knowledge Graph visualizes relationships between operational entities using graph-based representations.

It uses:

```text
NetworkX
Plotly
Streamlit Components
```

---

## ⚡ Digital Twin

The Digital Twin provides a simulation interface for the franchise network.

It can be used to explore operational scenarios across the outlet network.

---

## 🚨 Anomaly Scanner

The Anomaly Scanner performs anomaly detection across operational datasets.

It uses:

```text
Isolation Forest
```

and provides visual analytics for detected anomalies.

---

## 📡 Data Feed Center

The Data Feed Center provides direct record-ingestion functionality for operational data.

It interacts with the SQLite database through the application's database layer.

---

## 🛡️ Admin Dashboard

The Admin Dashboard provides platform-level management and monitoring.

It includes:

- User management
- Role assignment
- Database information
- Model/GPU information
- Operational statistics
- Outlet map
- System monitoring

---

# 🔐 Authentication

The application includes a complete authentication portal.

### Supported functions

- Login
- User registration
- Password hashing
- Failed-login tracking
- Account locking
- Password reset
- Email OTP
- Security-question recovery
- Password change
- Profile picture
- Account status

### Password Recovery

```text
Forgot Password
      ↓
 ┌───────────────┐
 │               │
 ▼               ▼
Email OTP    Security Question
 │               │
 └───────┬───────┘
         ▼
    New Password
```

OTP requests include resend cooldowns and expiration handling.

---

# 👥 Role-Based Access

The application supports four roles.

| Role | Main Access |
|---|---|
| **Admin** | Complete application |
| **Franchise Owner / Regional Ops Manager** | Operational modules + Data Feed Center |
| **Store Manager** | Copilot, Outlets, Inventory, Sentiment, Notifications, Translation |
| **Staff** | Copilot, Inventory, Notifications |

Access is controlled through `rbac.py`.

The application also performs route-level access checks to prevent unauthorized navigation.

---

# 🏗️ Architecture

```text
┌──────────────────────────────────────────────┐
│                Streamlit UI                 │
│                                              │
│ Home • Copilot • Agents • Analytics • Admin │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│              Authentication / RBAC           │
│                                              │
│ Login • Signup • OTP • Roles • Profiles     │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│              AI Orchestration                │
│                                              │
│             Intent Router                    │
└───────────────┬──────────────────────────────┘
                │
        ┌───────┴────────┐
        ▼                ▼
┌───────────────┐  ┌────────────────┐
│ ML / SQL      │  │ Hybrid RAG     │
│ Agents        │  │ FAISS + BM25   │
└───────┬───────┘  └───────┬────────┘
        │                  │
        └─────────┬────────┘
                  ▼
        ┌────────────────────┐
        │    Qwen 2.5 LLM    │
        │  Generation Layer  │
        └─────────┬──────────┘
                  ▼
        ┌────────────────────┐
        │    SQLite Data     │
        └────────────────────┘
```

---

# 🤖 LLM Backend

The application supports a local FastAPI AI backend.

### Primary model

```text
Qwen/Qwen2.5-3B-Instruct
```

### Fallback model

```text
Qwen/Qwen2.5-1.5B-Instruct
```

The application attempts to use GPU acceleration when available.

### FastAPI endpoints

```text
GET  /health
POST /generate
POST /stream
POST /translate
```

The backend runs on:

```text
http://localhost:8000
```

---

# 🗃️ Database

The application uses SQLite.

The database is initialized by:

```text
db.py
```

and populated using:

```text
seed_data.py
```

### Main data groups

The database contains franchise and logistics-related information such as:

- Users
- Chat history
- Outlets
- Staff
- Inventory
- Marketing
- Customer feedback
- Audits
- Ports
- Shipments
- Weather risks
- Alerts
- Carriers
- Customers
- Freight quotes
- Customs tariffs
- ML metrics

The seed process generates demonstration data for the application.

---

# 🎨 Aurora Command UI

The application uses a custom dark visual system implemented in:

```text
ui_theme.py
```

The Streamlit theme uses:

- Dark background
- Teal accent
- Glass-style interface elements
- Aurora-inspired gradients
- Custom cards
- Command-bar navigation
- Interactive analytics
- Modern dashboard layouts

The Streamlit theme configuration is stored in:

```text
.streamlit/config.toml
```

---

# 📁 Project Structure

```text
FranchiseOps_AI_Aurora_Redesign_FIXED.ipynb
│
└── franchise_app/
    │
    ├── app.py
    ├── admin_dash.py
    ├── ai_copilot.py
    ├── auth.py
    ├── rbac.py
    ├── config.py
    ├── db.py
    ├── seed_data.py
    │
    ├── intent_router.py
    ├── llm_engine.py
    ├── model_server.py
    ├── rag_engine.py
    ├── translation_engine.py
    │
    ├── agent1_franchise.py
    ├── agent2_franchise.py
    ├── agent3_franchise.py
    ├── agent4_marketing.py
    ├── agent5_sentiment.py
    ├── agent6_audit.py
    ├── agent7_digest.py
    ├── agent8_alerts.py
    ├── agent8_translation.py
    ├── agent9_pdf_rag.py
    │
    ├── anomaly_scanner.py
    ├── digital_twin.py
    ├── knowledge_graph.py
    ├── notifications.py
    ├── data_feed_center.py
    ├── report_generator.py
    ├── user_profile.py
    ├── weather_context.py
    ├── home_page.py
    ├── ui_theme.py
    │
    ├── requirements.txt
    │
    └── .streamlit/
        └── config.toml
```

---

# ⚙️ Installation

## 1. Open the notebook

Open:

```text
FranchiseOps_AI_Aurora_Redesign_FIXED.ipynb
```

in Google Colab or a Jupyter environment.

## 2. Run the notebook cells

Run the cells from top to bottom.

The notebook creates the `franchise_app` directory and writes the application modules into it.

## 3. Install dependencies

From inside the generated application directory:

```bash
cd franchise_app
pip install -r requirements.txt
```

## 4. Initialize the database

```bash
python -c "from db import init_db; from seed_data import seed_all; init_db(); seed_all()"
```

## 5. Start the application

```bash
streamlit run app.py
```

---

# ☁️ Google Colab

The notebook is designed to run in Google Colab.

It can:

- Mount Google Drive
- Create the application directory
- Install dependencies
- Initialize the SQLite database
- Generate seed data
- Start the FastAPI backend
- Launch Streamlit
- Create a Cloudflare tunnel for public access

The application stores persistent runtime data under the configured `FranchiseOps_AI` directory when Google Drive is available.

---

# 📦 Dependencies

The application uses the following main packages:

```text
streamlit
streamlit-option-menu
streamlit-folium
folium
deep-translator
transformers
torch
sentencepiece
accelerate
pdfplumber
reportlab
fpdf
bcrypt
flask
plotly
```

The exact dependency list is also generated inside:

```text
franchise_app/requirements.txt
```

---

# 🔑 Configuration

The application can use environment variables for model and email configuration.

### Hugging Face

```text
HF_TOKEN
HUGGINGFACE_TOKEN
```

### Email / OTP

The application accepts:

```text
GMAIL_ADDRESS
GMAIL_APP_PASSWORD
```

or:

```text
EMAIL_ID
EMAIL_PASSWORD
EMAIL_ADDRESS
EMAIL_APP_PASSWORD
```

### Data directory

```text
FRANCHISEOPS_DATA_DIR
```

If no custom data directory is supplied, the application uses its default runtime location.

---

# 📊 Data Generation

`seed_data.py` generates demonstration data for the application.

The generated dataset contains records for:

```text
50 outlets
150 staff records
150 inventory records
50 marketing campaigns
100 customer feedback records
100 shipments
20 weather-risk records
50 alerts
50 freight quotes
24 customers
6 carriers
6 customs tariff categories
```

This allows the application to demonstrate its analytical and visualization features without requiring an external production database.

---

# 🔄 Application Startup

When `app.py` starts, it:

```text
Start Streamlit
      ↓
Initialize SQLite
      ↓
Seed demonstration data
      ↓
Pre-warm Qwen
      ↓
Pre-warm NLLB-200
      ↓
Show authentication
      ↓
Authenticate user
      ↓
Apply RBAC
      ↓
Load Aurora Command UI
      ↓
Launch selected module
```

---

# 📍 Runtime Data

The application maintains runtime directories for:

```text
franchise_database.db
faiss_index/
bm25_index/
pdfs/
st_cache/
```

These locations are created automatically when required.

---

# ⚠️ Notes

- GPU acceleration is used when a compatible CUDA environment is available.
- The Qwen model requires significant memory compared with the rest of the application.
- NLLB-200 is loaded lazily/cached for translation.
- The PDF RAG functionality depends on the availability of the required FAISS/BM25 indexes.
- Demonstration data is generated by `seed_data.py`.

---

# 🏁 Project Summary

FranchiseOps AI brings multiple operational intelligence capabilities into a single interface:

```text
             FRANCHISEOPS AI
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
     Agents       Copilot       RAG
       │            │            │
       ▼            ▼            ▼
      ML         Qwen 2.5    FAISS + BM25
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
            Operational Intelligence
```

The result is a unified AI operations platform for exploring franchise performance, predicting risks, analyzing customers and inventory, retrieving information from documents, translating SOPs, monitoring anomalies, and supporting operational decision-making.
