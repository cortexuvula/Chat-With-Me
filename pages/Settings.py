import streamlit as st
import os
from dotenv import load_dotenv, set_key

# Load environment variables
dotenv_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

st.title("Settings")

# Initialize session state variables if they don't exist
if 'host' not in st.session_state:
    st.session_state['host'] = os.getenv("HOST", "")
if 'user' not in st.session_state:
    st.session_state['user'] = os.getenv("USER", "")
if 'password' not in st.session_state:
    st.session_state['password'] = os.getenv("PASSWORD", "")

# Input fields for HOST, USER, and PASSWORD
host = st.text_input("HOST", value=st.session_state['host'])
user = st.text_input("USER", value=st.session_state['user'])
password = st.text_input("PASSWORD", value=st.session_state['password'], type="password")

# Save settings to session state and .env file
if st.button("Save Settings"):
    st.session_state['host'] = host
    st.session_state['user'] = user
    st.session_state['password'] = password

    # Update .env file
    set_key(dotenv_path, "HOST", host)
    set_key(dotenv_path, "USER", user)
    set_key(dotenv_path, "PASSWORD", password)

    # Display success popup for 5 seconds
    placeholder = st.empty()
    placeholder.success("Settings saved!")
    import time
    time.sleep(5)
    placeholder.empty()

