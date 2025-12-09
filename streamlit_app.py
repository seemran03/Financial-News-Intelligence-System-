"""
Streamlit Web Interface for Financial News Intelligence System
"""
import streamlit as st
import json
from datetime import datetime
from typing import List, Dict
import pandas as pd

from src.workflow import FinancialNewsWorkflow
from src.agents.storage_agent import StorageAgent

# Page config
st.set_page_config(
    page_title="Financial News Intelligence System",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def initialize_workflow():
    """Initialize workflow (cached)"""
    return FinancialNewsWorkflow()


@st.cache_resource
def initialize_storage():
    """Initialize storage (cached)"""
    return StorageAgent()


def format_date(dt):
    """Format datetime"""
    if isinstance(dt, str):
        return dt
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def display_query_results(response):
    """Display query results in a nice format"""
    st.subheader("📊 Query Results")
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Results", response.total_results)
    with col2:
        st.metric("Companies Found", len(response.entity_breakdown.companies))
    with col3:
        st.metric("Sectors", len(response.entity_breakdown.sectors))
    with col4:
        st.metric("Regulators", len(response.entity_breakdown.regulators))
    
    # Reasoning
    st.info(f"🧠 **Reasoning:** {response.reasoning}")
    
    # Entity breakdown
    with st.expander("📋 Entity Breakdown", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            if response.entity_breakdown.companies:
                st.write("**Companies:**")
                st.write(", ".join(response.entity_breakdown.companies))
            if response.entity_breakdown.sectors:
                st.write("**Sectors:**")
                st.write(", ".join(response.entity_breakdown.sectors))
        with col2:
            if response.entity_breakdown.regulators:
                st.write("**Regulators:**")
                st.write(", ".join(response.entity_breakdown.regulators))
            if response.entity_breakdown.events:
                st.write("**Events:**")
                st.write(", ".join(response.entity_breakdown.events))
    
    # Impact summary
    st.success(f"💡 **Impact Summary:** {response.impact_summary}")
    
    # Results
    st.subheader("📰 Articles")
    for i, result in enumerate(response.results, 1):
        with st.container():
            st.markdown(f"### {i}. {result.headline}")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**Summary:** {result.summary}")
                st.caption(f"**Match Reason:** {result.match_reason}")
            with col2:
                st.metric("Relevance", f"{result.relevance_score:.3f}")
            
            # Stock impacts
            if result.stock_impacts:
                impacts_df = pd.DataFrame([
                    {
                        "Symbol": imp.symbol,
                        "Confidence": f"{imp.confidence:.2f}",
                        "Type": imp.type,
                        "Reason": imp.reason
                    }
                    for imp in result.stock_impacts
                ])
                with st.expander(f"📈 Stock Impacts ({len(result.stock_impacts)})"):
                    st.dataframe(impacts_df, use_container_width=True)
            
            st.divider()


def main():
    """Main Streamlit app"""
    # Header
    st.markdown('<p class="main-header">🚀 Financial News Intelligence System</p>', unsafe_allow_html=True)
    
    # Initialize
    workflow = initialize_workflow()
    storage = initialize_storage()
    
    # Sidebar
    with st.sidebar:
        st.header("🎛️ Navigation")
        page = st.radio(
            "Choose a page",
            ["📥 Process News", "🔍 Query News", "📊 View Database", "ℹ️ About"],
            label_visibility="collapsed"
        )
        
        st.divider()
        st.header("📈 Quick Stats")
        all_news = storage.get_all_news(limit=1000)
        st.metric("Articles in DB", len(all_news))
    
    # Main content
    if page == "📥 Process News":
        st.header("📥 Process News Articles")
        st.write("Upload or input financial news articles to process through the intelligence pipeline.")
        
        # Input method selection
        input_method = st.radio(
            "Input Method",
            ["📝 Manual Input", "📄 JSON Upload", "📋 Batch Input"],
            horizontal=True
        )
        
        if input_method == "📝 Manual Input":
            with st.form("manual_input_form"):
                headline = st.text_input("Headline *")
                content = st.text_area("Content *", height=200)
                source = st.text_input("Source", value="Manual Input")
                date = st.date_input("Date", value=datetime.now().date())
                time = st.time_input("Time", value=datetime.now().time())
                
                submitted = st.form_submit_button("🚀 Process Article", use_container_width=True)
                
                if submitted:
                    if headline and content:
                        article = {
                            "headline": headline,
                            "content": content,
                            "source": source,
                            "date": datetime.combine(date, time)
                        }
                        
                        with st.spinner("Processing article through pipeline..."):
                            result = workflow.process_news([article])
                        
                        if result['processed_news']:
                            st.success(f"✅ Successfully processed and stored article!")
                            st.json({
                                "Story ID": result['processed_news'][0].story_id,
                                "Headline": result['processed_news'][0].headline,
                                "Companies": result['processed_news'][0].entities.companies,
                                "Sectors": result['processed_news'][0].entities.sectors,
                                "Stock Impacts": len(result['processed_news'][0].stock_impacts)
                            })
                        else:
                            st.error("❌ Failed to process article. Check errors.")
                            if result['errors']:
                                for error in result['errors']:
                                    st.error(error)
                    else:
                        st.warning("⚠️ Please fill in headline and content.")
        
        elif input_method == "📄 JSON Upload":
            uploaded_file = st.file_uploader("Upload JSON file", type=['json'])
            
            if uploaded_file:
                try:
                    data = json.load(uploaded_file)
                    st.success(f"✅ Loaded {len(data)} articles from file")
                    
                    # Convert date strings
                    for article in data:
                        if isinstance(article.get('date'), str):
                            try:
                                article['date'] = datetime.fromisoformat(article['date'])
                            except:
                                article['date'] = datetime.now()
                    
                    if st.button("🚀 Process All Articles", use_container_width=True):
                        with st.spinner("Processing articles through pipeline..."):
                            result = workflow.process_news(data)
                        
                        st.success(f"✅ Processed {len(result['processed_news'])} articles!")
                        
                        # Show summary
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Ingested", len(result['ingested_articles']))
                        with col2:
                            st.metric("Deduplicated", len(result['consolidated_stories']))
                        with col3:
                            st.metric("Stored", len(result['processed_news']))
                        
                        if result['errors']:
                            st.warning(f"⚠️ {len(result['errors'])} errors encountered")
                            with st.expander("View Errors"):
                                for error in result['errors']:
                                    st.error(error)
                except Exception as e:
                    st.error(f"❌ Error loading file: {str(e)}")
        
        elif input_method == "📋 Batch Input":
            st.text_area(
                "Enter JSON array of articles",
                height=300,
                help="Format: [{\"headline\": \"...\", \"content\": \"...\", \"source\": \"...\", \"date\": \"...\"}]",
                key="batch_input"
            )
            
            if st.button("🚀 Process Batch", use_container_width=True):
                try:
                    data = json.loads(st.session_state.batch_input)
                    with st.spinner("Processing batch..."):
                        result = workflow.process_news(data)
                    st.success(f"✅ Processed {len(result['processed_news'])} articles!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    elif page == "🔍 Query News":
        st.header("🔍 Query News Database")
        st.write("Ask intelligent questions about the stored financial news.")
        
        # Query input
        query = st.text_input(
            "Enter your query",
            placeholder="e.g., 'HDFC Bank news', 'Banking sector update', 'RBI policy changes'",
            key="query_input"
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            search_button = st.button("🔍 Search", use_container_width=True)
        with col2:
            max_results = st.slider("Max Results", 1, 20, 10)
        
        if search_button and query:
            with st.spinner("Searching and analyzing..."):
                try:
                    response = workflow.query_news(query)
                    display_query_results(response)
                except Exception as e:
                    st.error(f"❌ Query error: {str(e)}")
        elif search_button:
            st.warning("⚠️ Please enter a query.")
        
        # Example queries
        st.subheader("💡 Example Queries")
        example_queries = [
            "HDFC Bank news",
            "Banking sector update",
            "RBI policy changes",
            "Interest rate impact",
            "IT sector developments",
            "SEBI regulations",
        ]
        
        cols = st.columns(3)
        for i, example in enumerate(example_queries):
            with cols[i % 3]:
                if st.button(example, key=f"example_{i}", use_container_width=True):
                    st.session_state.query_input = example
                    st.rerun()
    
    elif page == "📊 View Database":
        st.header("📊 Database Overview")
        
        all_news = storage.get_all_news(limit=100)
        
        if all_news:
            st.metric("Total Articles", len(all_news))
            
            # Filter options
            col1, col2 = st.columns(2)
            with col1:
                search_filter = st.text_input("🔍 Search headlines", key="db_search")
            with col2:
                sort_by = st.selectbox("Sort by", ["Date (Newest)", "Date (Oldest)", "Headline"])
            
            # Filter and sort
            filtered_news = all_news
            if search_filter:
                filtered_news = [n for n in filtered_news if search_filter.lower() in n.headline.lower()]
            
            if sort_by == "Date (Newest)":
                filtered_news = sorted(filtered_news, key=lambda x: x.date, reverse=True)
            elif sort_by == "Date (Oldest)":
                filtered_news = sorted(filtered_news, key=lambda x: x.date)
            else:
                filtered_news = sorted(filtered_news, key=lambda x: x.headline)
            
            st.metric("Filtered Results", len(filtered_news))
            
            # Display articles
            for article in filtered_news[:20]:  # Show first 20
                with st.expander(f"📰 {article.headline}"):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**Date:** {format_date(article.date)}")
                        st.write(f"**Source:** {', '.join(article.sources) if isinstance(article.sources, list) else article.sources}")
                        st.write(f"**Content:** {article.content[:500]}...")
                    with col2:
                        entities = article.entities if isinstance(article.entities, dict) else {}
                        if entities.get('companies'):
                            st.write("**Companies:**")
                            st.write(", ".join(entities['companies'][:5]))
                        if entities.get('sectors'):
                            st.write("**Sectors:**")
                            st.write(", ".join(entities['sectors']))
        else:
            st.info("📭 No articles in database. Process some news first!")
    
    elif page == "ℹ️ About":
        st.header("ℹ️ About the System")
        
        st.markdown("""
        ### 🚀 AI-Powered Financial News Intelligence System
        
        This system processes, deduplicates, analyzes, and queries financial news articles using a 
        multi-agent LangGraph workflow.
        
        #### 🎯 Key Features
        
        - **🔍 Intelligent Deduplication**: Semantic similarity-based duplicate detection
        - **🏷️ Entity Extraction**: Companies, sectors, regulators, people, events
        - **📈 Stock Impact Mapping**: Maps news to stock symbols with confidence scores
        - **💾 Dual Storage**: Vector DB (ChromaDB) + SQL for metadata
        - **🧠 Intelligent Queries**: Context-aware query processing with reasoning
        
        #### 🏗️ Architecture
        
        The system uses 6 specialized agents:
        1. **News Ingestion Agent** - Cleans and normalizes raw news
        2. **Deduplication Agent** - Detects semantic duplicates
        3. **Entity Extraction Agent** - Extracts structured entities
        4. **Stock Impact Analysis Agent** - Maps news to stocks
        5. **Storage & Indexing Agent** - Stores embeddings + metadata
        6. **Query Processing Agent** - Handles intelligent queries
        
        #### 📚 Usage
        
        - **Process News**: Upload or input news articles to process through the pipeline
        - **Query News**: Ask intelligent questions about stored news
        - **View Database**: Browse all processed articles
        
        #### 🔧 Technical Stack
        
        - LangGraph for multi-agent workflow
        - Sentence Transformers for embeddings
        - ChromaDB for vector storage
        - SQLAlchemy for metadata storage
        - spaCy for entity extraction
        - Streamlit for web interface
        """)
        
        st.divider()
        st.caption("Built with ❤️ using modern AI/ML tools")


if __name__ == "__main__":
    main()


