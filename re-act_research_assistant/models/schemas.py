from typing_extensions import TypedDict

class React_state(TypedDict):
    question: str
    thoughts: list[str]
    search_queries: list[str]
    retrieved_chunks: list[list[str]]
    observations: list[str]
    is_solved: bool
    iteration: int
    max_iterations: int
    final_answer: str