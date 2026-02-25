# 🛡️ Support Intelligence Core: Enterprise GraphRAG Platform

![Status](https://img.shields.io/badge/Status-Production--Ready-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Neo4j](https://img.shields.io/badge/Database-Neo4j%20Graph-green)
![LLM](https://img.shields.io/badge/AI-Llama%203.3--70B-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)

## 📌 Project Statement
This platform automates the construction of dynamic **Knowledge Graphs** from unstructured enterprise support data. By integrating **RAG pipelines**, **Vector Embeddings**, and **Semantic Search**, the system enables technical leads and executives to uncover hidden relationships across 8,600+ records.

---

## 📸 System Preview
![Intelligence Dashboard](./assets/dashboard_preview.png)
> **Figure 1:** *The Intelligence Dashboard showing real-time KPI tracking and RAG-powered pattern analysis.*

---

## 🏗️ System Architecture (Modules Implemented)
The project is structured into **modular layers** to ensure scalability and data security. 

### 1. [Module 1: Data Ingestion & Processing](./docs/preprocessing.md)
*Source Folder:* `src/module1_ingestion/`
- **Normalization:** Cleans and formats raw CSV ticket data.
- **Security:** Automated **PII Masking** to obfuscate customer emails for GDPR compliance.

### 2. [Module 2: Entity & Relationship Extraction](./docs/extraction.md)
*Source Folder:* `src/module2_extraction/`
- **Agentic Parsing:** Uses Llama-3.1-8B to extract 5-word summaries, root causes, and sentiment markers.
- **Data Enrichment:** Creates structured JSON triples for graph construction.

### 3. [Module 3: Graph Construction & Storage](./docs/ingestion.md)
*Source Folder:* `src/module3_graph_construction/`
- **Knowledge Mapping:** Stitches the graph using `(Customer)-[:RAISED]->(Ticket)-[:ABOUT]->(Product)`.
- **Indexing:** Provisions Neo4j Vector Indexes for 384-dimension cosine similarity search.

### 4. [Module 4: Intelligence Dashboard & RAG Engine](./docs/dashboard.md)
*Source Folder:* `src/module4_rag/` & `src/module5_dashboard/`
- **Hybrid Retrieval:** Orchestrates Vector similarity search with Graph context.
- **BI Visuals:** Direct Cypher-to-Plotly integration for zero-latency analytics.

---

## 🏁 Milestones & Project Progress

| Milestone | Objective | Status | Key Deliverable |
| :--- | :--- | :--- | :--- |
| **M1** | Data Ingestion & Schema | ✅ | PII Masking & Neo4j Vector Schema |
| **M2** | Entity Extraction & Building | ✅ | 8.6k Knowledge Triples Ingested |
| **M3** | Semantic Search & RAG | ✅ | Vector similarity-based contextual Q&A |
| **M4** | Dashboard & Deployment | ✅ | Live Streamlit Intelligence Portal |

---

## 📊 Knowledge Graph Visualization
The system preserves interaction context using a **Property Graph Model**.

![Knowledge Graph Schema](./assets/graph_preview.png)
> **Figure 2:** *Neo4j Graph View: Visualizing relationships between Support Tickets, Customers, and Products.*

---

## 🛠️ Infrastructure & Setup

### 1. Configuration (`.env`)
```env
NEO4J_URI=bolt://your-connection-url:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-secure-password
GROQ_API_KEY=gsk_your_api_key_here


2. Execution Pipeline
python -m src.module1_ingestion.normalize_tickets # Clean Data
python -m src.module2_extraction.entity_extractor  # AI Extraction
python -m src.module3_graph_construction.graph_builder # Ingest Graph
python -m src.module4_rag.create_vector_index    # Build Brain
streamlit run src/module5_dashboard/app.py       # Launch UI