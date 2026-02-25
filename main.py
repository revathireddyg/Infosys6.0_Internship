from src.module1_preprocess.preprocessor import run_preprocess_pipeline
from src.module1_schema.schema_builder import define_graph_schema
import os

def main():
    input_path = 'data/customer_support_tickets.csv'
    
    # Step 1: Preprocess 
    cleaned_df = run_preprocess_pipeline(input_path)
    
    # Step 2: Schema Design 
    # This prepares the map for Neo4j/LLM extraction
    graph_schema = define_graph_schema(cleaned_df)
    
    print("\n✅ Milestone 1 Complete: Data Ingested & Schema Defined.")

if __name__ == "__main__":
    main()