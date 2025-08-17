
from state import models
from langchain_core.messages import SystemMessage, AIMessage
# from llm import gemini
from tools.tools import get_tools
from utils import prompt as systemprompt
from utils.logger import logger


# system_prompt = systemprompt.system_prompt()
system_prompt = systemprompt.calender_prompt()
llm = get_tools()[1]
AgentState = models.EventData


def call_llm(state: AgentState) -> AgentState:
    """Function to call the LLM with the current state."""
    logger.info("=== CALLING LLM ===")
    messages = list(state['messages'])
    messages = [SystemMessage(content=str(system_prompt))] + messages
    message = llm.invoke(messages)
    messages.append(AIMessage(content=message.content))
    return {'messages': [message]}