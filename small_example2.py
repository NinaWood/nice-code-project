import os
import subprocess
import sys

# Ensure Streamlit is installed
try:
    import streamlit as st
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    print("Streamlit installed. Please restart the script.")
    sys.exit()

# Streamlit app
st.title("Hello, Streamlit! 👋")
st.write("This is a simple app to test Streamlit deployment.")

streamlit run random_quote_app.py

import streamlit as st
import requests

# Title of the app
st.title("Random Quote Generator 💬")
st.write("Click the button below to get a random inspirational quote.")

# Function to fetch a random quote
def fetch_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            quote = data.get("content", "No quote available.")
            author = data.get("author", "Unknown")
            return f"“{quote}” — {author}"
        else:
            return "Failed to fetch a quote. Please try again later."
    except Exception as e:
        return f"An error occurred: {e}"

# Button to generate a random quote
if st.button("Get a Random Quote"):
    quote = fetch_quote()
    st.write(quote)