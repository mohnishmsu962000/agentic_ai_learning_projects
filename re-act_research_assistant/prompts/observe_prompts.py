
def generate_observe_prompt(chunks: list[str]) -> str:
    """Generate prompt for observing/summarizing retrieved chunks"""
    
    formatted_chunks = "\n\n".join(f"Chunk {i+1}:\n{chunk}" for i, chunk in enumerate(chunks))
    
    return f"""You retrieved these chunks from a knowledge base:

{formatted_chunks}

Analyze what key information these chunks contain. Summarize the important facts, dates, numbers, or details.

Be specific and factual. Don't add information that isn't in the chunks.

Provide:
- summary: A concise summary of what information was found in these chunks"""