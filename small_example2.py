import streamlit as st
import requests

st.title("Random Quote Generator 💬")

def fetch_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f"“{data['content']}” — {data['author']}"
    else:
        return "Could not fetch a quote right now. 😔"

if st.button("Get a Random Quote"):
    st.write(fetch_quote())