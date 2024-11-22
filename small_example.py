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
st.title("Guess the Number Game 🎲")

# Generate a random number
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

# User Input
st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess")

# Feedback
if st.button("Submit Guess"):
    if user_guess < st.session_state.random_number:
        st.write("Too low! Try again. ⬇️")
    elif user_guess > st.session_state.random_number:
        st.write("Too high! Try again. ⬆️")
    else:
        st.write("🎉 Correct! You guessed it!")
        # Reset the game
        if st.button("Play Again"):
            st.session_state.random_number = random.randint(1, 100)