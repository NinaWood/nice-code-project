import requests
import streamlit as st

st.title("AI-Generated Illustrations")

prompt = st.text_input("Enter a prompt for the illustration:", "A futuristic cityscape")
if st.button("Generate"):
    # Example API call to AI image generator
    response = requests.post("https://api.openai.com/v1/images", json={"prompt": prompt})
    st.image(response.json()["image_url"], caption=f"Generated for: {prompt}")