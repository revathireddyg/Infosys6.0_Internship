from neo4j import GraphDatabase
import json
import os
from dotenv import load_dotenv

load_dotenv()

class KnowledgeGraphManager:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"), 
            auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
        )

    def upload_data(self, json_file):
        """Maps JSON keys to Neo4j nodes and creates 'rag_content'."""
        with open(json_file, 'r') as f:
            data = json.load(f)

        with self.driver.session() as session:
            for item in data:
                # Use exact keys from your dataset
                t_id = str(item.get('Ticket ID'))
                c_name = item.get('Customer Name', 'User')
                p_name = item.get('Product Purchased', 'Product')
                
                # THE RICH CONTEXT: This is the 'story' the AI reads in chat
                rich_text = (
                    f"Ticket {t_id} regarding {p_name}. Customer: {c_name}. "
                    f"Description: {item.get('Ticket Description')}. "
                    f"Root Cause: {item.get('root_cause')}. Sentiment: {item.get('sentiment')}."
                )

                session.run("""
                    MERGE (c:Customer {email: $email}) SET c.name = $name
                    MERGE (p:Product {name: $pname})
                    MERGE (t:Ticket {id: $tid})
                    SET t.rag_content = $rich_text, t.status = $status, t.priority = $priority, t.name = $tid
                    
                    MERGE (c)-[:RAISED]->(t)
                    MERGE (t)-[:ABOUT]->(p)
                """, 
                email=item.get('Customer Email'), name=c_name, pname=p_name, 
                tid=t_id, rich_text=rich_text, status=item.get('Ticket Status'), 
                priority=item.get('Ticket Priority'))
            
            print(f"✅ Stitched {len(data)} nodes into the knowledge web.")

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    manager = KnowledgeGraphManager()
    # Ensure this path matches your extractor output
    manager.upload_data('data/extracted_triples.json')
    manager.close()