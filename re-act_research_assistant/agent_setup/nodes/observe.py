from langchain_openai import ChatOpenAI
from models.schemas import React_state
from pydantic import BaseModel
from prompts.observe_prompts import generate_observe_prompt
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))

class Result_state(BaseModel):
    summary: str

structured_llm = llm.with_structured_output(Result_state)



def observe_node(state: React_state) -> dict: 
    
    latest_chunks = state['retrieved_chunks'][-1]
    
    result = structured_llm.invoke(generate_observe_prompt(latest_chunks))
    
    return {
        'observations': state['observations'] + [result.summary]
    }