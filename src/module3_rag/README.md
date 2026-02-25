# 🤖 Module 3: GraphRAG Logic & AI Integration

## 📝 Overview
Module 3 implements the **Retrieval-Augmented Generation (RAG)** architecture. Unlike standard RAG that only uses flat text, our **GraphRAG** approach queries the Neo4j Knowledge Graph to retrieve high-context relationships, which are then processed by the LLM to provide accurate, data-driven answers.

## 🛠️ The RAG Pipeline
1. **Natural Language Input:** The user asks a question in the dashboard.
2. **Cypher Generation:** The system uses an LLM to translate the English question into a Neo4j Cypher query.
3. **Graph Retrieval:** The query is executed against the Neo4j database to fetch relevant facts and relationships.
4. **Augmented Response:** The retrieved data is sent back to the LLM (Groq Llama-3) to generate a human-friendly summary.



## ⌨️ AI & LLM Configuration
We utilize **LangChain** to orchestrate the communication between the database and the LLM.

### 1. LLM Integration (Groq)
We use the `llama-3.1-8b-instant` model via the Groq API for ultra-fast inference speeds.

```python
# Core LLM Initialization
llm = ChatGroq(
    temperature=0, 
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)




2. Graph Chain Logic
The GraphCypherQAChain allows the AI to "speak" Cypher and navigate our schema:

chain = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True # Required for dynamic Cypher execution
)


