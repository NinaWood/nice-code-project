import streamlit as st
from PIL import Image
import numpy as np

# App title
st.title("Image Grayscaler 🖤")

# Instructions
st.write("Upload an image, and I'll convert it to grayscale!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    st.subheader("Original Image:")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to grayscale
    grayscale_image = image.convert("L")
    st.subheader("Grayscale Image:")
    st.image(grayscale_image, caption="Grayscale Image", use_column_width=True)

    # Download button for the grayscale image
    st.subheader("Download Grayscale Image:")
    grayscale_array = np.array(grayscale_image)
    result = Image.fromarray(grayscale_array)
    result.save("grayscale_image.png")

    with open("grayscale_image.png", "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name="grayscale_image.png",
            mime="image/png",
        )

import matplotlib.pyplot as plt

# Add histogram for the uploaded image
if uploaded_file is not None:
    # Display histogram for the original image
    st.subheader("Original Image Histogram:")
    original_hist = np.array(image)
    fig, ax = plt.subplots()
    ax.hist(original_hist.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    st.pyplot(fig)

    # Display histogram for the grayscale image
    st.subheader("Grayscale Image Histogram:")
    grayscale_hist = np.array(grayscale_image)
    fig, ax = plt.subplots()
    ax.hist(grayscale_hist.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
    st.pyplot(fig)
