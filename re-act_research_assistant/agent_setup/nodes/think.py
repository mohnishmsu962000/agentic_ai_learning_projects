from models.schemas import React_state
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from prompts.think_prompts import get_initial_prompt, get_followup_prompt
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

llm = ChatOpenAI(model = 'gpt-4o-mini',temperature=0, openai_api_key = os.getenv('OPENAI_API_KEY'))


class ThinkingOutput(BaseModel):
    reasoning: str
    search_query: str
    
    
structured_llm = llm.with_structured_output(ThinkingOutput)


def think_node(state: React_state) -> dict:
    question = state['question']
    observations = state['observations']
    
    
    if not observations: 
        result = structured_llm.invoke(get_initial_prompt(question))
        search_query = result.search_query
        thought = result.reasoning
        
    else:
        formatted_observations = chr(10).join(f"- {obs}" for obs in observations)
        result = structured_llm.invoke(get_followup_prompt(question, formatted_observations))
        search_query = result.search_query
        thought = result.reasoning
    
    
    
    return {
        'search_queries': state['search_queries'] + [search_query],
        'thoughts': state['thoughts'] + [thought],
        'iteration': state['iteration'] + 1
    }