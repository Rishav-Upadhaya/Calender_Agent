from state import models
from tools import tools

# tool_calls = tools.get_tools()
AgentState = models.EventData

def should_continue(state: AgentState):
    """Determine if the agent should continue based on the last message."""
    
    result = state["messages"][-1]
    return hasattr(result, "tool_calls") and len(result.tool_calls) > 0