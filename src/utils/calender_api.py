from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials



def get_calendar_service(token_json="tokens/token.json"):
    creds = Credentials.from_authorized_user_file(
        token_json, scopes=["https://www.googleapis.com/auth/calendar"]
    )
    service = build("calendar", "v3", credentials=creds)
    return service

