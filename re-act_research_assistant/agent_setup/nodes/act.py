from models.schemas import React_state
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma(
    persist_directory="./chroma_data",
    embedding_function=OpenAIEmbeddings()
)

def act_node(state: React_state) -> dict:
    
    search_query = state['search_queries'][-1]
    
   
    results = vectorstore.similarity_search(search_query, k=5)
    
    chunks = [doc.page_content for doc in results]
    
    return {
        'retrieved_chunks': state['retrieved_chunks'] + [chunks]
    }