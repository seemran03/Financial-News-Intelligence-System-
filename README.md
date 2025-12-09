# Financial-News-Intelligence-System-
This project is a complete AI-driven workflow that processes, deduplicates, and analyzes financial news using a LangGraph multi-agent architecture. It extracts actionable insights for traders and investors by combining NLP, embeddings, and semantic search.
# 🚀 AI-Powered Financial News Intelligence System

A sophisticated multi-agent system built with LangGraph that processes, deduplicates, analyzes, and queries financial news articles with intelligent entity extraction and stock impact mapping.

## 📋 Overview

This system ingests raw financial news, removes semantic duplicates, extracts entities (companies, sectors, regulators, people, events), maps stock impacts, and provides intelligent query capabilities with context-aware reasoning.

### Key Features

- **🔍 Intelligent Deduplication**: Uses semantic similarity (embeddings) to detect and merge duplicate articles
- **🏷️ Entity Extraction**: Extracts companies, sectors, regulators, people, and financial events
- **📈 Stock Impact Mapping**: Maps news to stock symbols with confidence scores
- **💾 Dual Storage**: Vector database (ChromaDB) for semantic search + SQL for metadata
- **🧠 Intelligent Queries**: Context-aware query processing with sector expansion and reasoning
- **🔄 Multi-Agent Workflow**: LangGraph-based orchestration of 6 specialized agents

## 🏗️ System Architecture

The system uses a **LangGraph multi-agent workflow** with 6 specialized agents:

1. **News Ingestion Agent** - Cleans and normalizes raw news
2. **Deduplication Agent** - Detects semantic duplicates using embeddings
3. **Entity Extraction Agent** - Extracts structured entities using spaCy NER
4. **Stock Impact Analysis Agent** - Maps news to stock symbols with confidence
5. **Storage & Indexing Agent** - Stores embeddings + metadata
6. **Query Processing Agent** - Handles intelligent queries with reasoning

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy model:**
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Run the demo:**
   ```bash
   python main.py
   ```

## 🚀 Quick Start

### 1. Verify Installation

```bash
python verify_installation.py
```

### 2. Run the Demo

```bash
python main.py
```

This will:
- Process sample financial news articles
- Demonstrate deduplication
- Show entity extraction
- Display stock impact mapping
- Run example queries

### 3. Use the Interactive Query CLI

```bash
python utils/query_cli.py
```

### 4. Launch Web Interfaces

**Streamlit Interface:**
```bash
streamlit run streamlit_app.py
```
Then open your browser to `http://localhost:8501`

**Gradio Interface:**
```bash
python gradio_app.py
```
Then open your browser to `http://localhost:7860`

### Processing News Articles (Programmatic)

```python
from src.workflow import FinancialNewsWorkflow
from datetime import datetime

# Initialize workflow
workflow = FinancialNewsWorkflow()

# Prepare news articles
news_articles = [
    {
        "headline": "RBI increases repo rate by 25 basis points",
        "content": "The Reserve Bank of India has announced...",
        "source": "Financial Times",
        "date": datetime.now()
    },
    # ... more articles
]

# Process through pipeline
result = workflow.process_news(news_articles)
```

### Querying News (Programmatic)

```python
# Query the stored news
response = workflow.query_news("HDFC Bank news")

# Access results
print(f"Found {response.total_results} articles")
print(f"Reasoning: {response.reasoning}")
for result in response.results:
    print(f"- {result.headline} (relevance: {result.relevance_score:.3f})")
```

## 🌐 Web Interfaces

The project includes two modern web interfaces for easy interaction:

### Streamlit Interface

A feature-rich dashboard with multiple pages:
- **📥 Process News**: Upload or input news articles (manual, JSON, or batch)
- **🔍 Query News**: Intelligent query interface with example queries
- **📊 View Database**: Browse and search all processed articles
- **ℹ️ About**: System information and documentation

**Launch:**
```bash
streamlit run streamlit_app.py
```

### Gradio Interface

A clean, tabbed interface with:
- **📥 Process News**: Single article or batch JSON processing
- **🔍 Query News**: Natural language querying with results table
- **📊 View Database**: Database overview with filtering
- **ℹ️ About**: System documentation

**Launch:**
```bash
python gradio_app.py
```

Both interfaces provide:
- ✅ Real-time processing feedback
- ✅ Visual results display
- ✅ Entity breakdown visualization
- ✅ Stock impact mapping
- ✅ JSON export capabilities

## 📊 Example Queries

The system supports various query types:

| Query Type | Example | Behavior |
|------------|---------|----------|
| **Company Query** | "HDFC Bank news" | Direct articles + sector-related |
| **Sector Query** | "Banking sector update" | All bank-related news |
| **Regulator Query** | "RBI policy changes" | Regulator-specific news |
| **Thematic Query** | "Interest rate impact" | Rate-related stories |
| **Hybrid Query** | "Banking impact of RBI rate hike" | Multi-entity reasoning |

## 🎯 System Capabilities

### Deduplication
- Uses cosine similarity on embeddings (threshold: 0.85)
- Clusters duplicates into consolidated stories
- Retains information from all merged articles

### Entity Extraction
- **Companies**: Direct mentions + stock symbol mapping
- **Sectors**: Banking, IT, Pharma, Auto, FMCG, Energy
- **Regulators**: RBI, SEBI, FED, IRDAI
- **People**: Named entity recognition
- **Events**: Rate hikes, dividends, acquisitions, earnings, etc.

### Stock Impact Mapping
- **Direct mentions**: Confidence = 1.0
- **Sector-wide**: Confidence = 0.6-0.8
- **Regulator impact**: Dynamic confidence based on relevance

### Query Processing
- Semantic search using embeddings
- Entity-based filtering
- Sector expansion
- Context-aware reasoning
- Impact summary generation

## 📁 Project Structure

```
assignment project/
├── src/
│   ├── agents/
│   │   ├── ingestion_agent.py      # News ingestion & cleaning
│   │   ├── deduplication_agent.py   # Semantic deduplication
│   │   ├── entity_extraction_agent.py  # Entity extraction
│   │   ├── stock_impact_agent.py    # Stock impact mapping
│   │   ├── storage_agent.py         # Storage & indexing
│   │   └── query_agent.py           # Query processing
│   ├── models.py                    # Data models
│   └── workflow.py                  # LangGraph workflow
├── examples/                        # Sample data
├── utils/                           # Utility scripts
├── tests/                           # Unit tests
├── config.py                        # Configuration
├── main.py                          # Demo script
├── streamlit_app.py                 # Streamlit web interface
├── gradio_app.py                    # Gradio web interface
├── requirements.txt                 # Dependencies
└── README.md                        # This file
```

## 🔧 Configuration

Edit `config.py` to customize:

- **Embedding model**: Change `EMBEDDING_MODEL` (default: "all-MiniLM-L6-v2")
- **Similarity threshold**: Adjust `SIMILARITY_THRESHOLD` (default: 0.85)
- **Stock symbols**: Add more companies to `STOCK_SYMBOLS_MAPPING`
- **Sectors**: Extend `SECTOR_KEYWORDS`
- **Confidence scores**: Modify `CONFIDENCE_SCORES`

## 📈 Evaluation Metrics

The system is designed to achieve:
- ✅ Deduplication accuracy ≥ 95%
- ✅ Entity extraction precision ≥ 90%
- ✅ Context-aware query relevance
- ✅ Logical stock impact mapping

## 🎨 Features & Design Decisions

### Why LangGraph?
- Clean separation of concerns
- Easy to extend with new agents
- Visual workflow representation
- State management built-in

### Why Dual Storage?
- **ChromaDB**: Fast semantic search with embeddings
- **SQL**: Reliable metadata storage and complex queries
- Best of both worlds

### Human Touches
- Comprehensive error handling
- Progress logging
- Detailed reasoning in query responses
- Clean, readable code with comments
- Example data and demos included
- **Modern web interfaces** (Streamlit + Gradio) for easy interaction
- Interactive query examples and suggestions
- Visual data display with tables and metrics

## 🚧 Future Enhancements (Optional)

- [ ] Sentiment analysis
- [ ] Price impact estimation
- [ ] Cross-sector supply chain impact
- [ ] Explainability of retrieval
- [ ] Multilingual (Hindi) support
- [ ] Real-time RSS feed processing
- [x] Web dashboard (Streamlit + Gradio) ✅
- [ ] API endpoints
- [ ] Advanced visualizations and charts
- [ ] Export capabilities (PDF, CSV)

## 📝 Notes

- The system uses lightweight models for fast processing
- All data is stored locally (ChromaDB + SQLite)
- No external API keys required
- Designed for educational/demonstration purposes

## 🤝 Contributing

Feel free to extend this system with additional features, agents, or improvements!

## 📄 License

This project is created for educational purposes as part of an assignment.

---

**Built with ❤️ using LangGraph, LangChain, and modern AI/ML tools**

