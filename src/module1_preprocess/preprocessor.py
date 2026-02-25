import pandas as pd
import datetime
import numpy as np

def run_preprocess_pipeline(file_path):
    print(f"--- Starting Preprocessing for: {file_path} ---")
    
    # 1. LOAD & DEDUPLICATE
    df = pd.read_csv(file_path)
    df = df.drop_duplicates(subset=['Ticket ID'])

    # 2. DATA CLEANING (Imputation instead of Dropping)
    # Filling missing text so the Knowledge Graph remains connected
    df['Ticket Subject'] = df['Ticket Subject'].fillna('Unknown Subject')
    df['Ticket Description'] = df['Ticket Description'].fillna('No description provided.')
    df['Resolution'] = df['Resolution'].fillna('Active/In-Progress')
    df['Customer Satisfaction Rating'] = df['Customer Satisfaction Rating'].fillna(0)

    # 3. DATA TRANSFORMATION
    df['Date of Purchase'] = pd.to_datetime(df['Date of Purchase'])
    df['Time to Resolution'] = pd.to_datetime(df['Time to Resolution'], errors='coerce')
    df['Ticket Priority'] = df['Ticket Priority'].str.lower()

    # 4. DATA ENRICHMENT
    # Metric: Resolution speed
    df['Resolution_Time_Hours'] = (df['Time to Resolution'] - df['Date of Purchase']).dt.total_seconds() / 3600
    df['Resolution_Time_Hours'] = df['Resolution_Time_Hours'].apply(lambda x: round(x, 2) if x > 0 else 0)

    # 5.Segment: Customer demographics
    df['Customer_Segment'] = df['Customer Age'].apply(
        lambda x: 'Youth' if x < 30 else ('Adult' if x < 50 else 'Senior')
    )

    # 6. SECURITY & METADATA
    # Masking Email for PII protection
    df['Customer Email'] = df['Customer Email'].apply(lambda x: str(x)[0] + "***" + str(x)[str(x).find('@'):])
    df['ingestion_timestamp'] = datetime.datetime.now()

    print(f"✅ Preprocessing Complete! Total records preserved: {len(df)}")
    return df