"""
Configuration settings for the Financial News Intelligence System
"""
import os
from pathlib import Path
from typing import Dict, List

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"
DB_DIR = PROJECT_ROOT / "chroma_db"

# Create directories if they don't exist
for dir_path in [DATA_DIR, MODELS_DIR, LOGS_DIR, DB_DIR]:
    dir_path.mkdir(exist_ok=True)

# Embedding model configuration
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Fast and efficient for semantic similarity
EMBEDDING_DIMENSION = 384

# Deduplication threshold
SIMILARITY_THRESHOLD = 0.85  # Cosine similarity threshold for duplicates

# Entity extraction
SPACY_MODEL = "en_core_web_sm"  # Lightweight NER model

# Stock symbol mapping
STOCK_SYMBOLS_MAPPING = {
    # Banking sector
    "HDFC Bank": "HDFCBANK",
    "HDFC": "HDFCBANK",
    "ICICI Bank": "ICICIBANK",
    "ICICI": "ICICIBANK",
    "State Bank of India": "SBIN",
    "SBI": "SBIN",
    "Axis Bank": "AXISBANK",
    "Kotak Mahindra Bank": "KOTAKBANK",
    "Kotak Bank": "KOTAKBANK",
    "Punjab National Bank": "PNB",
    "Bank of Baroda": "BANKBARODA",
    "IndusInd Bank": "INDUSINDBK",
    
    # IT sector
    "TCS": "TCS",
    "Tata Consultancy Services": "TCS",
    "Infosys": "INFY",
    "Wipro": "WIPRO",
    "HCL Technologies": "HCLTECH",
    "HCL": "HCLTECH",
    "Tech Mahindra": "TECHM",
    
    # Pharma
    "Sun Pharma": "SUNPHARMA",
    "Sun Pharmaceutical": "SUNPHARMA",
    "Dr. Reddy's": "DRREDDY",
    "Dr Reddy's": "DRREDDY",
    "Cipla": "CIPLA",
    "Lupin": "LUPIN",
    
    # Auto
    "Maruti Suzuki": "MARUTI",
    "Tata Motors": "TATAMOTORS",
    "Mahindra": "M&M",
    "Mahindra & Mahindra": "M&M",
    "Bajaj Auto": "BAJAJ-AUTO",
    
    # FMCG
    "Hindustan Unilever": "HINDUNILVR",
    "HUL": "HINDUNILVR",
    "ITC": "ITC",
    "Nestle": "NESTLEIND",
    
    # Energy
    "Reliance Industries": "RELIANCE",
    "Reliance": "RELIANCE",
    "ONGC": "ONGC",
    "Oil and Natural Gas Corporation": "ONGC",
}

# Sector keywords for impact detection
SECTOR_KEYWORDS = {
    "Banking": ["bank", "banking", "lender", "loan", "credit", "deposit", "NPA", "NPAs", "bad loans"],
    "IT": ["IT", "software", "technology", "digital", "tech", "IT services", "outsourcing"],
    "Pharma": ["pharma", "pharmaceutical", "drug", "medicine", "FDA", "clinical trial"],
    "Auto": ["automobile", "auto", "vehicle", "car", "SUV", "two-wheeler"],
    "FMCG": ["FMCG", "consumer goods", "fast-moving", "retail"],
    "Energy": ["oil", "gas", "petroleum", "refinery", "crude", "energy"],
}

# Regulator keywords
REGULATOR_KEYWORDS = {
    "RBI": ["RBI", "Reserve Bank", "Reserve Bank of India", "central bank", "repo rate", "CRR", "SLR"],
    "SEBI": ["SEBI", "Securities and Exchange Board", "market regulator", "insider trading"],
    "FED": ["Federal Reserve", "Fed", "FOMC", "US central bank"],
    "IRDAI": ["IRDAI", "Insurance Regulatory", "insurance regulator"],
}

# Confidence score ranges
CONFIDENCE_SCORES = {
    "direct_mention": 1.0,
    "sector_high": 0.8,
    "sector_medium": 0.6,
    "regulator_high": 0.7,
    "regulator_medium": 0.5,
}

# Database configuration
DATABASE_URL = f"sqlite:///{PROJECT_ROOT}/financial_news.db"
CHROMA_COLLECTION_NAME = "financial_news_embeddings"

# Query processing
MAX_QUERY_RESULTS = 10
QUERY_EXPANSION_ENABLED = True


