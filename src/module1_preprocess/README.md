# 🧹 Module 1.1: Data Preprocessing

## 📝 Overview
The Preprocessing module is responsible for the "ETL" (Extract, Transform, Load) foundation. It ensures the data is clean before the LLM or Graph Database ever sees it.

## 🛠️ Key Operations
* **Text Normalization:** Removing noise and special characters from ticket descriptions.
* **Sentiment Scoring:** Applying initial sentiment labels to provide context for the Knowledge Graph.
* **Data Formatting:** Standardizing dates and categorical fields into a uniform structure.



## 📂 File Description
* `preprocess_data.py`: Main cleaning script.
* `sentiment_analysis.py`: Logic for automated sentiment categorization.

---
**Next Step:** [Go to Module 1.2: Schema Modeling ➡️](../module1_schema/README.md)