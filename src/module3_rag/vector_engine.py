import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

class RAGManager:
    def __init__(self):
        # 1. Initialize Neo4j Driver
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"), 
            auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
        )
        # 2. Load the same embedding model used for the index
        # 'all-MiniLM-L6-v2' is fast and accurate for 100-16,000 tickets.
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def similarity_search(self, query, top_k=5):
        """
        Converts query to vector and finds the 'Rich Context' in Neo4j.
        """
        # Convert user's question into a numerical vector
        query_vector = self.embeddings.embed_query(query)
        
        with self.driver.session() as session:
            # SEARCH LOGIC: This queries the 'ticket_vectors' index we created
            # It returns the Ticket ID and the 'rag_content' (The Full Story)
            result = session.run("""
                CALL db.index.vector.queryNodes('ticket_vectors', $k, $vector)
                YIELD node, score
                RETURN node.id AS id, node.rag_content AS text, score
            """, vector=query_vector, k=top_k).data()
            
            return result

    def close(self):
        """Safely close the connection."""
        self.driver.close()

if __name__ == "__main__":
    # Quick Test to verify the engine is 'On-Point'
    rag = RAGManager()
    try:
        test_query = "Who has issues with GoPro?"
        print(f"🔍 Testing Search: '{test_query}'")
        matches = rag.similarity_search(test_query, top_k=2)
        for m in matches:
            print(f"🎯 Match Found (ID: {m['id']}): {m['text'][:100]}...")
    finally:
        rag.close()