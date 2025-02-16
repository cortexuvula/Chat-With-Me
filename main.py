import logging
import streamlit as st
from streamlit_float import *
import requests
import uuid
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)  # enable debug logging

# Load environment variables and initialize float layout
load_dotenv() 
float_init()  

# Retrieve and clean environment variables (remove surrounding quotes)
HOST = os.getenv("HOST", "").strip('"')
USER = os.getenv("USER", "").strip('"')
PASSWORD = os.getenv("PASSWORD", "").strip('"')

# Initialize chat history, sessionID, and chat input state
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'sessionID' not in st.session_state:
    st.session_state['sessionID'] = str(uuid.uuid4())
if 'chat_input' not in st.session_state:
    st.session_state['chat_input'] = ""

# Layout containers
header = st.container()
body = st.container()
user_input = st.container()
user_input.float("bottom: 0; position: fixed; padding: 20px; background-color: rgba(0, 0, 0, 1); ")  # added padding to user_input


# Callback function for Send button
def send_message():
    
    if st.session_state.chat_input:
        webhook_url = HOST  # use HOST from .env
        payload = {"chatInput": st.session_state.chat_input, "sessionID": st.session_state['sessionID']}
        try:
            response = requests.post(webhook_url, json=payload, auth=(USER, PASSWORD))  # use env variables
            if response.status_code == 200:
                reply = response.json().get("output", "No reply received")
            else:
                reply = f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            reply = f"Request failed: {e}"
        st.session_state['messages'].append({"user": st.session_state.chat_input, "bot": reply})
        st.session_state.chat_input = ""  # clear the input field
        

# Callback function for New Session button
def new_session():
    st.session_state['sessionID'] = str(uuid.uuid4())
    st.session_state['messages'] = []

# Layout Containers: header, body (chat history), input
with header:
    st.title("Chat with Me")

with body:
    for msg in st.session_state['messages']:
        st.write(f"Question: {msg['user']}")
        st.write(f"Answer: {msg['bot']}")

with user_input:
    st.markdown(
        """
        <style>
        div[data-testid="stTextInput"] > div {
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.text_input("Enter your message:", key="chat_input", on_change=send_message)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Send", on_click=send_message)
    with col2:
        st.button("New Session", on_click=new_session)


