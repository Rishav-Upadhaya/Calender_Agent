from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage
from operator import add as add_messages


class EventData(TypedDict):
    intent: str
    title: str
    start_time: str
    end_time: str
    attendees: str = ""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    