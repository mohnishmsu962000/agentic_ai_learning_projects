from langgraph.graph import StateGraph, START, END
from agent_setup.nodes.act import act_node
from agent_setup.nodes.answer import answer_node
from agent_setup.nodes.observe import observe_node
from agent_setup.nodes.think import think_node
from agent_setup.evaluate import evaluate_node
from models.schemas import React_state

graph = StateGraph(React_state)

graph.add_node('act', act_node)
graph.add_node('answer', answer_node)
graph.add_node('observe', observe_node)
graph.add_node('think', think_node)
graph.add_node('evaluate', evaluate_node)


graph.add_edge(START, 'think')
graph.add_edge('think', 'act')
graph.add_edge('act', 'observe')
graph.add_edge('observe', 'evaluate')

def evaluate_condition(state: React_state):
    if state['is_solved']:
        return 'approved'
    elif state['iteration'] >= state['max_iterations']:
        return 'approved'
    else:
        return 'not-approved'
    
graph.add_conditional_edges('evaluate',
                            evaluate_condition,
                            {
                                'approved': 'answer',
                                'not-approved': 'think'
                            }
                            )

graph.add_edge('answer', END)

workflow = graph.compile()