def get_initial_prompt(question: str) -> str:
    """Prompt for first iteration when no observations exist"""
    return f"""You are researching this question: {question}

What information do you need to answer this question? 

Explain your reasoning for what you need to search for, then generate a specific search query.

Provide:
- reasoning: Why you need this information and what it will help answer
- search_query: The specific query to search for (be concise and targeted)"""


def get_followup_prompt(question: str, formatted_observations: str) -> str:
    """Prompt for later iterations with past observations"""
    return f"""You are researching this question: {question}

What you've found so far:
{formatted_observations}

Analyze what's still missing to fully answer the question.

Provide:
- reasoning: What information is missing and why you need it
- search_query: The specific query to search for the missing information"""