import streamlit as st
import requests

# App title
st.title("Random Quote Generator 💬")
st.write("Click the button below to get a random inspirational quote.")

# Function to fetch quotes from ZenQuotes API
def fetch_quote():
    try:
        # Fetch random quote from ZenQuotes API
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            quote = data[0]["q"]  # Quote text
            author = data[0]["a"]  # Author
            return f"“{quote}” — {author}"
        else:
            return "Failed to fetch a quote. Please try again later."
    except Exception as e:
        return f"An error occurred: {e}"

# Button to fetch a random quote
if st.button("Get a Random Quote"):
    quote = fetch_quote()
    st.write(quote)