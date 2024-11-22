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
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Simple Visualization")

# Create DataFrame
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Display Bar Chart
st.write("Bar Chart of Categories:")
fig, ax = plt.subplots()
ax.bar(df["Category"], df["Values"])
st.pyplot(fig)
