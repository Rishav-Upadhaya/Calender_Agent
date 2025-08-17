from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import json

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Use the downloaded credentials.json
flow = InstalledAppFlow.from_client_secrets_file("google_credentials.json", SCOPES)
creds = flow.run_local_server(port=0)

# Save the token for later use
with open("token.json", "w") as f:
    f.write(creds.to_json())

print("token.json generated successfully!")
