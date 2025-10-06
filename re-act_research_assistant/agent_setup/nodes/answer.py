from langchain_openai import ChatOpenAI
from models.schemas import React_state
from pydantic import BaseModel
from prompts.answer_prompts import generate_answer_prompt
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'

load_dotenv(env_path)

class Answer(BaseModel):
    answer: str

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))

structured_llm = llm.with_structured_output(Answer)

def answer_node(state: React_state) -> dict:
    question = state['question']
    observations = state['observations']  # Read the findings
    
    answer = structured_llm.invoke(generate_answer_prompt(question, observations)).answer
    
    return {"final_answer": answer}