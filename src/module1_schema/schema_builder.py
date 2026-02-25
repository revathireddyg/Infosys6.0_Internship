from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

def setup_database_schema():
    driver = GraphDatabase.driver(
        os.getenv("NEO4J_URI"), 
        auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
    )
    
    with driver.session() as session:
        print("🏗️ Configuring Neo4j Schema...")
        # Prevent duplicate nodes
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (c:Customer) REQUIRE c.email IS UNIQUE")
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (t:Ticket) REQUIRE t.id IS UNIQUE")
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (p:Product) REQUIRE p.name IS UNIQUE")
        
        # Initialize Vector Index for the AI to 'search' the graph
        session.run("""
            CREATE VECTOR INDEX ticket_vectors IF NOT EXISTS
            FOR (t:Ticket) ON (t.rag_content)
            OPTIONS {indexConfig: {`vector.dimensions`: 384, `vector.similarity_function`: 'cosine'}}
        """)
    print("✅ Schema and Vector Index are ready.")
    driver.close()

if __name__ == "__main__":
    setup_database_schema()