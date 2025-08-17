# Calender_Agent (Agent_Share)

Agent_Share automates the addition of IPO events to your Google Calendar, including reminders for each event.

## Features

- Automatically adds IPO events to your calendar.
- Provides direct links to Google Calendar events.
- Sets reminders for IPO eavents at 9:00 AM on the start date.

## Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (for dependency and environment management)
- Google account (for calendar integration)
- Google Calendar API credentials (see below)

## Obtaining Google API Credentials & Generating Token

1. **Get Google Calendar API credentials:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Navigate to **APIs & Services > Library** and enable the **Google Calendar API**.
   - Go to **APIs & Services > Credentials**.
   - Click **Create Credentials** > **OAuth client ID**.
   - Choose **Desktop app** as the application type.
   - Download the `credentials.json` file and place it in your project directory.

2. **Generate the token:**
   - Run the following command to execute `generate_token.py`:
     ```bash
     uv run src/generate_token.py
     ```
   - Follow the authentication flow in your browser. After successful authentication, a `token.json` file will be created in your project directory.

3. **Proceed to run the main application as described above.**

## Project Structure

```
Calender_Agent/
├── src/
│   └── main.py
├── requirements.txt
├── README.md
└── ...
```

## Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rishav-Upadhaya/Calender_Agent.git
   cd Calender_Agent
   ```

2. **Initialize environment and install dependencies:**
   ```bash
   uv init
   uv venv
   uv sync
   ```

3. **Run the application:**
   ```bash
   uv run src/main.py
   ```

4. **Follow the prompts** to add IPO events to your calendar.

## Example Output

```
OK. I've added the IPO events to your calendar:

* Swastik Laghubitta Bittiya Sanstha Limited IPO: [Google Calendar Link]
* Sagar Distillery Limited IPO (for foreign employment citizens): [Google Calendar Link]
* Mabilung Energy Limited IPO: [Google Calendar Link]

Reminders are set for 9:00 AM on the start date of each IPO.
```

## Troubleshooting

- If you encounter authentication issues, ensure you are logged into your Google account and have granted necessary permissions.
- For issues with `uv`, refer to the [uv documentation](https://github.com/astral-sh/uv).
