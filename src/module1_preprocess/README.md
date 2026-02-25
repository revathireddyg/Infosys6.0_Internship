# 🧹 Module 1: Data Ingestion & Processing Layer
**Path:** `src/module1_ingestion/normalize_tickets.py`

## 🎯 Purpose
The ingestion layer serves as the "Gatekeeper" of the platform. Raw enterprise support data is often inconsistent, missing critical values, or contains sensitive **PII (Personally Identifiable Information)**. This module ensures that every record is sanitized, secured, and mathematically enriched before it reaches the AI Extraction or the Knowledge Graph stages.



---

## 🛠️ Key Technical Implementations

### 1. Enterprise Security (PII Masking)
To comply with global data privacy standards (like GDPR), we implemented automated email obfuscation. This ensures that while we can uniquely identify a customer node in the graph, their actual contact information is protected.

**The Logic:**
```python
# From normalize_tickets.py
df['Customer Email'] = df['Customer Email'].apply(
    lambda x: str(x)[0] + "***" + str(x)[str(x).find('@'):]
)


2. Feature Engineering & Enrichment
We transformed raw timestamps and age data into actionable technical metrics to allow for better "Multi-hop" graph queries:

Resolution_Time_Hours: Calculates the precise window between purchase and resolution by subtracting timestamps.

Customer_Segment: Uses a lambda function to cluster users into demographics:

Youth: < 30

Adult: 30 - 50

Senior: 50+

3. Data Integrity & Imputation
Instead of dropping rows with missing values (which would cause "Isolated Islands" in our Knowledge Graph), we used Imputation to maintain connectivity:

Missing Text: Filled with "Unknown Subject" or "No description provided."

Missing Ratings: Defaulted to 0 to avoid calculation errors in the dashboard.