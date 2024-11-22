import os
import subprocess
import sys

# Ensure Streamlit is installed
try:
    import streamlit as st
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    import streamlit as st

st.title("Hello, Streamlit! 👋")
st.write("This is a simple app to test Streamlit deployment.")
# Add your code below...
#import streamlit as st

import streamlit as st
import random

# Set up the title

import subprocess
import sys

try:
    import matplotlib
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib