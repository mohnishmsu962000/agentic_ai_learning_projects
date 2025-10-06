from langchain_openai import ChatOpenAI
from models.schemas import React_state
from pydantic import BaseModel
from prompts.evaluate_prompts import generate_evaluate_prompt
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

class Is_solved_output(BaseModel):
    is_solved: bool
    reasoning: str

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))

structured_llm = llm.with_structured_output(Is_solved_output)

def evaluate_node(state: React_state) -> dict:
    question = state['question']
    observations = state['observations']
    
    result = structured_llm.invoke(generate_evaluate_prompt(question, observations))
    
    return {
        'is_solved': result.is_solved,
        'thoughts': state['thoughts'] + [result.reasoning]
    }
    
    