import pandas as pd
import json
import os
import time
import re
import math
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

INPUT_FILE = 'data/cleaned_tickets.csv'
OUTPUT_FILE = 'data/extracted_triples.json'

def clean_value(val):
    """Replaces NaN/NaT with None for JSON compatibility."""
    if isinstance(val, float) and math.isnan(val):
        return None
    if pd.isna(val):
        return None
    return val

def run_ai_extraction(df):
    llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)
    template = """
    Analyze support ticket: "{text}"
    Return ONLY a JSON object:
    {{
      "issue_summary": "5-word summary",
      "root_cause": "Hardware/Software/Network/User",
      "sentiment": "Positive/Neutral/Negative"
    }}
    """
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = prompt | llm

    results = []
    print(f"🚀 AI Analyzing {len(df)} tickets...")
    for _, row in tqdm(df.iterrows(), total=df.shape[0]):
        try:
            response = chain.invoke({"text": row['Ticket Description']})
            match = re.search(r'\{.*\}', response.content, re.DOTALL)
            ai_data = json.loads(match.group()) if match else {}
            
            # Merge and Clean NaN
            record = {k: clean_value(v) for k, v in row.to_dict().items()}
            record.update(ai_data)
            results.append(record)
            time.sleep(0.4) 
        except:
            results.append({k: clean_value(v) for k, v in row.to_dict().items()})
    return results

if __name__ == "__main__":
    df = pd.read_csv(INPUT_FILE).head(100)
    extracted_data = run_ai_extraction(df)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(extracted_data, f, indent=4)
    print(f"✅ Intelligence saved to {OUTPUT_FILE}")