# FranchiseOps AI — RAG Knowledge Base & Operations Engine

An end-to-end Retrieval-Augmented Generation (RAG) pipeline built for Quick Service Restaurants (QSR) and franchise operations management. This tool automates the web scraping, PDF document processing, embedding generation, and vector search indexing for internal Standard Operating Procedures (SOPs), government regulations, food safety acts, and labor laws.

---

## 📌 Project Overview

**FranchiseOps AI** is designed to streamline franchise compliance, store-level operations, and training management by serving as an intelligent query system. 

Key capabilities include:
* **Multi-Source Data Scraping:** Automated extraction of text from web resources and PDF files.
* **Auto-Discovery Engine:** Automatically extracts PDF links linked inside HTML resources.
* **Custom Document Ingestion:** Supports interactive uploads and Google Drive drops for internal custom PDFs.
* **Vector Store Indexing:** Embeds document chunks using `all-MiniLM-L6-v2` and indexes them with **FAISS** for ultra-fast semantic retrieval.
* **Curated Knowledge Base:** Built-in standard QSR SOPs covering food safety (FSSAI/OSHA), cash handling, HR, POS outage protocols, and crisis management.

---

## 🛠 Tech Stack & Dependencies

* **Language:** Python 3.11+
* **Environment:** Google Colab / Jupyter Notebook
* **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
* **Vector Database:** `FAISS` (`faiss-cpu`)
* **Frameworks:** LangChain, BeautifulSoup4, PyMuPDF (`fitz`), requests, tqdm, textblob, vaderSentiment

---

## 📂 Google Drive Directory Structure

When executed on Google Colab, the notebook automatically configures the following output directories on Google Drive:

```text
/content/drive/MyDrive/FranchiseOps_AI/
│
├── rag_documents/        # Raw extracted .txt files and manifest.json
├── custom_pdfs/          # Drop folder for user-provided custom PDFs
└── faiss_index/          # Persisted FAISS vector store index files
```

---

## 🚀 Execution Pipeline

### 1. Requirements Installation & Drive Mount
Installs required packages (`langchain`, `faiss-cpu`, `pymupdf`, `sentence-transformers`, etc.) and mounts Google Drive.

### 2. Scraping & Data Harvesting
* **Phase 1:** Scrapes **116 HTML Web Sources** (e.g., FSSAI, OSHA, FDA, WHO, SHRM) and automatically identifies embedded PDF documents.
* **Phase 2:** Merges auto-discovered PDFs with **109 static PDF sources**.
* **Phase 3:** Downloads and parses text from PDFs using PyMuPDF.

### 3. Custom File Ingestion
Allows custom documents to be added to the RAG system via:
1. Interactive file upload prompt.
2. Scanning the `/custom_pdfs/` folder in Google Drive.

### 4. SOP Knowledge Base Integration
Appends 65 pre-curated store SOPs (IDs `KB-101` to `KB-165`) covering critical topics like minimum freezer temperatures, POS downtime workflows, allergen labeling, and POSH Act compliance.

### 5. Text Chunking & FAISS Vector Indexing
* Documents are split using `RecursiveCharacterTextSplitter` (chunk size: 1000, overlap: 100).
* Generates vector embeddings via `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`).
* Saves the FAISS vector index locally (`./franchiseops_faiss_index`) and syncs a copy to Google Drive.

---

## 💻 Usage & Query Interface

Once built, you can perform semantic similarity searches against the knowledge base:

```python
# Perform similarity search
query = "What is the minimum freezer temperature?"
results = vectorstore.similarity_search(query, k=3)

for rank, result in enumerate(results, start=1):
    print(f"--- Match {rank} ---")
    print(f"Content: {result.page_content}")
    print(f"Source: {result.metadata.get('source')} | ID: {result.metadata.get('id', 'N/A')}\n")
```

---

## 📝 Sample Knowledge Base Topics Covered

| SOP Category | Examples |
| :--- | :--- |
| **Food Safety & Cold Chain** | Freezer temp ≤ -18°C, quaternary ammonium sanitizer every 2h, FIFO. |
| **HR & Labor** | Minimum wage reviews, minor break laws, POSH Act committees. |
| **Store Operations** | Shift staffing, POS outage workflows, daily fryer oil filtering. |
| **Compliance & Escalation** | FSSAI penalties, viral complaint response time, glass breakage protocols. |
