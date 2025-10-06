from models.schemas import React_state
from agent_setup.graph import workflow

state = {
    'question': "What is the SOC2 certification date?",
    'thoughts': [],
    'search_queries': [],
    'retrieved_chunks': [],
    'observations': [],
    'is_solved': False,
    'iteration': 0,
    'max_iterations': 5,
    'final_answer': ''
}

result = workflow.invoke(state)
print(result['final_answer'])