# 🏗️ Module 2: Entity Extraction & Graph Ingestion

## 📝 Overview
Module 2 is the engine of the project. It takes the preprocessed data from Module 1 and executes the **Graph Ingestion Pipeline**. This process involves extracting entities and programmatically creating nodes and relationships within the Neo4j AuraDB cloud instance.

## 🛠️ Key Operations
* **Entity Mapping:** Identifying the core attributes of each record (e.g., Ticket ID, Customer Name, Sentiment).
* **Relationship Linkage:** Connecting disparate data points into a unified graph structure.
* **Batch Processing:** Efficiently pushing data to the cloud to minimize network latency.



## ⌨️ Core Cypher Ingestion Logic
To build the graph, we use the `MERGE` clause. This ensures that we create new nodes if they don't exist, or update existing ones, preventing duplicate data.

### 1. Creating Nodes and Links
This query creates the **Customer** and **Ticket** nodes and links them together:

```cypher
UNWIND $batch AS row
MERGE (c:Customer {customer_id: row.customer_id})
SET c.name = row.customer_name

MERGE (t:Ticket {ticket_id: row.ticket_id})
SET t.description = row.description,
    t.priority = row.priority,
    t.sentiment = row.sentiment

MERGE (c)-[:RAISED]->(t)



2. Mapping Categories
This query links tickets to their specific Product and Problem Category:
UNWIND $batch AS row
MATCH (t:Ticket {ticket_id: row.ticket_id})
MERGE (p:Product {name: row.product_name})
MERGE (cat:Category {type: row.problem_type})

MERGE (t)-[:BELONGS_TO]->(p)
MERGE (t)-[:CATEGORIZED_AS]->(cat)



📂 File Description
graph_manager.py: The Python driver that connects to Neo4j and executes the Cypher batches.

extraction_logic.py: Logic for mapping DataFrame rows to graph properties.