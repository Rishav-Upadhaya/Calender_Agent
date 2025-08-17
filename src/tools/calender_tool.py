# from utils.calender_api import get_calendar_service
from dotenv import load_dotenv
import os
from langchain_core.tools import tool

load_dotenv()

TIMEZONE = os.getenv("TIMEZONE", "Asia/Kathmandu")

# service = get_calendar_service()
@tool(description="Add an event to the calendar")
def add_event_to_calendar(service, title, start_time, end_time, attendees=[]):
    """Add an event to the Google Calendar."""
    event = {
        "summary": title,
        "start": {"dateTime": start_time, "timeZone": TIMEZONE},
        "end": {"dateTime": end_time, "timeZone": TIMEZONE},
        "attendees": [{"email": email} for email in attendees],
    }
    created_event = service.events().insert(calendarId="primary", body=event).execute()
    return created_event.get("htmlLink")