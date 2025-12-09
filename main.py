"""
Main entry point for the Financial News Intelligence System
"""
import json
from datetime import datetime
from src.workflow import FinancialNewsWorkflow
from src.models import NewsArticle


def print_separator():
    """Print a nice separator"""
    print("\n" + "="*80 + "\n")


def print_header(text: str):
    """Print a formatted header"""
    print(f"\n{'='*80}")
    print(f"  {text}")
    print(f"{'='*80}\n")


def demo_ingestion():
    """Demo: Ingest sample financial news"""
    print_header("📰 DEMO: News Ingestion & Processing")
    
    # Sample financial news articles (some with duplicates)
    sample_news = [
        {
            "headline": "RBI increases repo rate by 25 basis points",
            "content": "The Reserve Bank of India has announced a 25 basis point increase in the repo rate, bringing it to 6.5%. This move is expected to impact banking sector stocks and loan rates across the country.",
            "source": "Financial Times",
            "date": datetime(2024, 1, 15, 10, 0, 0),
            "url": "https://example.com/rbi-rate-hike-1"
        },
        {
            "headline": "Reserve Bank hikes interest rate by 0.25%",
            "content": "India's central bank has raised the policy rate by 25 bps to 6.5%. Banking stocks are likely to see volatility following this decision.",
            "source": "Economic Times",
            "date": datetime(2024, 1, 15, 11, 0, 0),
            "url": "https://example.com/rbi-rate-hike-2"
        },
        {
            "headline": "HDFC Bank reports strong Q3 earnings",
            "content": "HDFC Bank announced quarterly earnings that beat analyst expectations. The bank's net profit rose 18% year-on-year, driven by strong loan growth and improved asset quality.",
            "source": "Business Standard",
            "date": datetime(2024, 1, 16, 9, 0, 0),
            "url": "https://example.com/hdfc-earnings"
        },
        {
            "headline": "ICICI Bank and Axis Bank see surge in digital transactions",
            "content": "Major private sector banks including ICICI Bank and Axis Bank have reported a significant increase in digital transaction volumes. The banking sector continues to digitize rapidly.",
            "source": "Mint",
            "date": datetime(2024, 1, 17, 14, 0, 0),
            "url": "https://example.com/banking-digital"
        },
        {
            "headline": "SEBI announces new guidelines for insider trading",
            "content": "The Securities and Exchange Board of India has introduced stricter guidelines to prevent insider trading. All listed companies must comply with the new regulations by next quarter.",
            "source": "Livemint",
            "date": datetime(2024, 1, 18, 10, 0, 0),
            "url": "https://example.com/sebi-guidelines"
        },
        {
            "headline": "TCS wins major IT contract from US client",
            "content": "Tata Consultancy Services has secured a $500 million IT services contract from a major US corporation. This deal is expected to boost the company's revenue significantly.",
            "source": "Times of India",
            "date": datetime(2024, 1, 19, 8, 0, 0),
            "url": "https://example.com/tcs-contract"
        },
    ]
    
    # Initialize workflow
    workflow = FinancialNewsWorkflow()
    
    # Process news
    print("🔄 Processing news articles through the pipeline...\n")
    result = workflow.process_news(sample_news)
    
    # Display results
    print_separator()
    print(f"✅ Processing Complete!")
    print(f"   - Ingested: {len(result['ingested_articles'])} articles")
    print(f"   - Deduplicated: {len(result['consolidated_stories'])} unique stories")
    print(f"   - Processed: {len(result['processed_news'])} articles stored")
    
    if result['errors']:
        print(f"\n⚠️  Errors encountered: {len(result['errors'])}")
        for error in result['errors']:
            print(f"   - {error}")
    
    print_separator()
    
    # Show some details
    if result['processed_news']:
        print("\n📊 Sample Processed Article:")
        sample = result['processed_news'][0]
        print(f"   Headline: {sample.headline}")
        print(f"   Companies: {', '.join(sample.entities.companies) if sample.entities.companies else 'None'}")
        print(f"   Sectors: {', '.join(sample.entities.sectors) if sample.entities.sectors else 'None'}")
        print(f"   Regulators: {', '.join(sample.entities.regulators) if sample.entities.regulators else 'None'}")
        print(f"   Stock Impacts: {len(sample.stock_impacts)} symbols")
        for impact in sample.stock_impacts[:3]:
            print(f"      - {impact.symbol}: {impact.confidence:.2f} ({impact.type})")
    
    return workflow


def demo_query(workflow: FinancialNewsWorkflow):
    """Demo: Query the stored news"""
    print_header("🔍 DEMO: Intelligent Query Processing")
    
    queries = [
        "HDFC Bank news",
        "Banking sector update",
        "RBI policy changes",
        "Interest rate impact",
        "What are the latest IT sector developments?",
    ]
    
    for query in queries:
        print(f"\n💬 Query: '{query}'")
        print("-" * 80)
        
        try:
            response = workflow.query_news(query)
            
            print(f"\n📈 Results: {response.total_results} articles found")
            print(f"🧠 Reasoning: {response.reasoning}")
            
            if response.entity_breakdown.companies:
                print(f"🏢 Companies: {', '.join(response.entity_breakdown.companies)}")
            if response.entity_breakdown.sectors:
                print(f"📊 Sectors: {', '.join(response.entity_breakdown.sectors)}")
            if response.entity_breakdown.regulators:
                print(f"🏛️  Regulators: {', '.join(response.entity_breakdown.regulators)}")
            
            print(f"\n💡 Impact Summary: {response.impact_summary}")
            
            if response.results:
                print(f"\n📰 Top Results:")
                for i, result in enumerate(response.results[:3], 1):
                    print(f"\n   {i}. {result.headline}")
                    print(f"      Relevance: {result.relevance_score:.3f}")
                    print(f"      Match: {result.match_reason}")
                    print(f"      Summary: {result.summary[:150]}...")
                    if result.stock_impacts:
                        impacts_str = ", ".join([f"{imp.symbol} ({imp.confidence:.2f})" for imp in result.stock_impacts[:3]])
                        print(f"      Impacts: {impacts_str}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print_separator()


def main():
    """Main function"""
    print_header("🚀 AI-Powered Financial News Intelligence System")
    print("Welcome! This system processes, deduplicates, and analyzes financial news.")
    print("It uses a multi-agent LangGraph workflow to provide intelligent insights.\n")
    
    try:
        # Demo 1: Process news
        workflow = demo_ingestion()
        
        # Demo 2: Query news
        demo_query(workflow)
        
        print_header("✅ Demo Complete!")
        print("The system is ready for production use.")
        print("You can now:")
        print("  1. Process more news articles using workflow.process_news()")
        print("  2. Query stored news using workflow.query_news()")
        print("  3. Extend the system with additional features")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()


