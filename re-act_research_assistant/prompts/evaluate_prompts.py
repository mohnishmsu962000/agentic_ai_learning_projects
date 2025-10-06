def generate_evaluate_prompt(question: str, observations: list[str]) -> str:
    """Generate prompt for evaluating if question can be answered"""
    
    formatted_observations = "\n".join(f"- {obs}" for obs in observations)
    
    return f"""You are evaluating whether you have enough information to answer a question.

QUESTION: {question}

INFORMATION GATHERED SO FAR:
{formatted_observations}

Analyze:
1. What does the question ask for?
2. What information do you have from your searches?
3. Is there enough information to provide a complete answer?
4. If not, what specific information is still missing?

Provide:
- is_solved: true if you can confidently answer the question, false if you need more information
- reasoning: Explain what you have and what's missing (if anything)"""