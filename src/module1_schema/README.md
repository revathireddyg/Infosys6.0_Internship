# 🏗️ Module 1.2: Schema Modeling & Constraints

## 📝 Overview
This module defines the **Blueprint** of the Knowledge Graph. We use Neo4j to model complex relationships that traditional SQL databases cannot easily represent.

## 📐 Graph Schema & Relationships
We use a **Node-Edge** model to represent the technical support ecosystem:
* **Nodes:** `Ticket`, `Customer`, `Product`, `Agent`.
* **Relationships:** `(Customer)-[:RAISED]->(Ticket)`, `(Ticket)-[:HAS_ISSUE]->(ProblemType)`.



## ⌨️ Cypher Constraints
To ensure data integrity and performance, we implement the following constraints directly in the database:

```cypher
// 1. Ensure unique Ticket IDs
CREATE CONSTRAINT IF NOT EXISTS FOR (t:Ticket) 
REQUIRE t.ticket_id IS UNIQUE;

// 2. Ensure unique Customer IDs
CREATE CONSTRAINT IF NOT EXISTS FOR (c:Customer) 
REQUIRE c.customer_id IS UNIQUE;

// 3. Create Index for faster searching on Priority
CREATE INDEX IF NOT EXISTS FOR (t:Ticket) 
ON (t.priority);


---
**Next Step:** [Go to Module 2: Extraction ➡️](../module2_extraction/README.md)
