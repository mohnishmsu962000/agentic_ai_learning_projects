from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

DOCUMENTS = [
    """SECURITY & COMPLIANCE
ACME Corp achieved SOC2 Type II certification in March 2023. Our infrastructure is hosted on AWS with 256-bit AES encryption for data at rest. We maintain ISO 27001 compliance and undergo annual penetration testing by third-party security firms. GDPR compliance is maintained across all EU operations.""",
    
    """PRICING STRUCTURE
Our enterprise plan starts at $299 per user per month with volume discounts available for teams over 50 users. Annual contracts receive a 20% discount. Implementation fees are waived for contracts over $50,000 annually. Custom pricing is available for Fortune 500 clients requiring dedicated infrastructure.""",
    
    """IMPLEMENTATION TIMELINE
Standard implementation takes 4-6 weeks from contract signing. This includes data migration, user training, and integration with existing systems. Rush implementations (2-3 weeks) are available for an additional 30% fee. Our team provides 24/7 support during the implementation phase.""",
    
    """CUSTOMER SUCCESS STORIES
TechStartup Inc reduced their customer response time by 65% after implementing our platform in Q2 2024. FinanceCorp saw a 40% increase in team productivity within the first month. HealthCare Systems integrated our solution with their existing EHR system in just 3 weeks.""",
    
    """TECHNICAL SPECIFICATIONS
Our API supports REST and GraphQL protocols. SDK availability includes Python, JavaScript, Java, and Ruby. Maximum API rate limit is 10,000 requests per minute for enterprise plans. WebSocket support enables real-time data synchronization. All endpoints use OAuth 2.0 authentication.""",
    
    """COMPANY BACKGROUND
Founded in 2018 by former Google engineers, ACME Corp has raised $45M in Series B funding led by Sequoia Capital. Our team of 120 employees operates from offices in San Francisco, London, and Singapore. We serve over 500 enterprise clients across 40 countries."""
]

def setup_chromadb():
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    
    all_chunks = []
    for doc in DOCUMENTS:
        chunks = splitter.split_text(doc)
        all_chunks.extend(chunks)
    
    vectorstore = Chroma.from_texts(
        texts=all_chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory="./chroma_data"
    )
    
    print(f"ChromaDB initialized with {len(all_chunks)} chunks")
    return vectorstore

if __name__ == "__main__":
    setup_chromadb()