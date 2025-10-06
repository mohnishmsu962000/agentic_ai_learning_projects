
def generate_answer_prompt(question: str, observations: list[str]) -> str:
    """Generate prompt for creating final answer from all observations"""
    
    formatted_observations = "\n".join(f"- {obs}" for obs in observations)
    
    return f"""You have completed research on this question: {question}

Based on your research, here are your findings:
{formatted_observations}

Provide a comprehensive answer to the question using the information gathered.

Requirements:
- Use only information from the observations
- Be specific with facts, dates, numbers, and details
- Structure the answer clearly
- If information is incomplete, acknowledge what's missing

Provide:
- answer: A complete, well-structured response to the question"""