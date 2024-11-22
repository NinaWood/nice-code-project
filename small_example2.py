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

# Example of Streamlit logging output
st.write("Whatever you want to say, genius.")