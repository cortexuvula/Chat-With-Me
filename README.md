# Chat With Me

This project is a simple chat interface built with Streamlit that interacts with a N8N webhook with basic authorization requests.

## Features

- Chat interface built with Streamlit.
- Session management using UUIDs.
- API integration with a webhook.
- Environment configuration with python-dotenv.

## Setup

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   
   - Copy `env.example` to `.env` and update the variables:
     - `USER`
     - `PASSWORD`
     - `HOST`

3. **Run the Application:**

   ```bash
   streamlit run Chat.py
   ```

## File Overview

- **Chat.py**: Main application code which defines the chat interface.
- **Settings.py**: Change HOST, USER and PASSWORD 
- **.env**: Contains environment variables (keep this file secure).
- **env.example**: Example file for environment variables.
- **requirements.txt**: List of dependencies.
