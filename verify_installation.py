"""
Quick script to verify installation and dependencies
"""
import sys

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_imports():
    """Check if required packages can be imported"""
    packages = [
        ("langgraph", "LangGraph"),
        ("langchain", "LangChain"),
        ("sentence_transformers", "Sentence Transformers"),
        ("chromadb", "ChromaDB"),
        ("spacy", "spaCy"),
        ("sqlalchemy", "SQLAlchemy"),
        ("pydantic", "Pydantic"),
    ]
    
    failed = []
    for package, name in packages:
        try:
            __import__(package)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} not found")
            failed.append(name)
    
    return len(failed) == 0

def check_spacy_model():
    """Check if spaCy model is installed"""
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        print("✅ spaCy model (en_core_web_sm)")
        return True
    except OSError:
        print("❌ spaCy model (en_core_web_sm) not found")
        print("   Run: python -m spacy download en_core_web_sm")
        return False

def main():
    """Main verification"""
    print("🔍 Verifying Installation...\n")
    
    all_ok = True
    
    print("Python Version:")
    if not check_python_version():
        all_ok = False
    
    print("\nRequired Packages:")
    if not check_imports():
        all_ok = False
        print("\n   Install missing packages with: pip install -r requirements.txt")
    
    print("\nspaCy Model:")
    if not check_spacy_model():
        all_ok = False
    
    print("\n" + "="*50)
    if all_ok:
        print("✅ All checks passed! System is ready to use.")
        print("\nNext steps:")
        print("  1. Run: python main.py")
        print("  2. Or use: python utils/query_cli.py")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
    print("="*50)

if __name__ == "__main__":
    main()


