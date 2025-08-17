from state import models
from tools import tools
from langchain_core.messages import ToolMessage
from utils.logger import logger
from utils.calender_api import get_calendar_service



AgentState = models.EventData
tools_dict = tools.get_tools()[0]

def take_action(state: AgentState) -> AgentState:
    """Function to take action based on the current state."""
    
    tool_calls = state['messages'][-1].tool_calls
    logger.info(f"\n=== TOOL CALLS ===\n")
    results = []
    for t in tool_calls:
        tool_name = t['name'].strip()
        if tool_name not in tools_dict:
            logger.error(f"Tool: {tool_name} does not exist.")
            result = "Incorrect Tool Name, Please Retry and Select tool from List of Available tools."
        else:
            # For Getting the University
            if tool_name == "add_event_to_calendar":
                    logger.debug(f" ==== Invoking tool: {tool_name} ====")
                    result = tools_dict[tool_name].invoke({
                        "service": get_calendar_service(),
                        "title": t['args'].get('title'),
                        "start_time": t['args'].get('start_time'),
                        "end_time": t['args'].get('end_time'),
                        "attendees": t['args'].get('attendees', [])
                    })
            else:
                logger.debug(f"==== Invoking tool: {tool_name} ====")
                # For retrieval agent
                result = tools_dict[tool_name].invoke({})
            print(f"Result length: {len(str(result))}")
        results.append(ToolMessage(tool_call_id=t['id'], name=tool_name, content=str(result)))

    logger.info("Tools Execution Complete. Back to the model!")
    return {'messages': results}
    