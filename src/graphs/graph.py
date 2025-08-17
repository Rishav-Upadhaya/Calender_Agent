from langgraph.graph import StateGraph, END
from state import models
from graphs import call_llm, decider, router

AgentState = models.EventData

def rag_agent():
    graph = StateGraph(AgentState)
    graph.add_node("llm", call_llm.call_llm)
    graph.add_node("tool_router", router.take_action)

    graph.add_conditional_edges(
        "llm",
        decider.should_continue,
        {True: "tool_router", False: END}
    )
    graph.add_edge("tool_router", "llm")
    graph.set_entry_point("llm")

    rag_agent = graph.compile()

    return rag_agent