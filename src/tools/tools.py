from tools.calender_tool import add_event_to_calendar
from tools.scraping_tool import get_share_info
from llm import gemini


# module‑level LLM
base_llm = gemini.get_gemini()
# retriever_tool = retriever.retriever_tool()

def get_tools():
    tools = [add_event_to_calendar, get_share_info]

    # bind without shadowing
    bound_llm = base_llm.bind_tools(tools)

    tools_dict = {tool.name: tool for tool in tools}
    return tools_dict, bound_llm

