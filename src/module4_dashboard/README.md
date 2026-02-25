# 📊 Module 4: Interactive Analytics Dashboard

## 📝 Overview
Module 4 is the presentation layer of the Enterprise Intelligence system. Built using **Streamlit**, this interactive dashboard provides stakeholders with real-time visibility into the support ticket ecosystem, combining high-level KPIs with a deep-dive AI Chat interface.

## 🛠️ Key Features
* **Executive Summary KPIs:** Instant visibility into Total Tickets, Priority distribution, and overall Customer Sentiment.
* **Interactive Visualizations:** Dynamic charts powered by **Plotly** and **Altair** for trend analysis.
* **GraphRAG Chat Interface:** A natural language portal that allows users to query the Neo4j Knowledge Graph without writing Cypher code.
* **Real-time Data Streaming:** Direct connection to the Neo4j AuraDB cloud instance.



## 🎨 UI Architecture
The dashboard is organized into three primary sections:
1. **Sidebar:** Navigation and system status indicators.
2. **Analytics Tab:** Statistical breakdowns of ticket volume, product issues, and agent performance.
3. **AI Consultant Tab:** The GraphRAG chat interface for complex relationship-based queries.

[Image of a user interface wireframe showing layout for sidebar, main analytics area, and chat component]

## ⌨️ Implementation Highlights
We use Streamlit's state management to ensure a smooth, "single-page application" (SPA) feel.

### 1. The KPI Engine
Metrics are calculated dynamically by querying the graph to provide up-to-the-second accuracy:

```python
# Example of real-time metric calculation
total_tickets = graph.query("MATCH (t:Ticket) RETURN count(t) as count")[0]['count']
st.metric("Total Records", f"{total_tickets}")



2. The AI Integration
The dashboard connects directly to the RAG engine defined in Module 3:
if user_input := st.chat_input("Ask about the tickets..."):
    with st.spinner("Analyzing Graph Data..."):
        response = rag_chain.run(user_input)
        st.write(response)


