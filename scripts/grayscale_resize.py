import streamlit as st
from PIL import Image

# App title
st.title("Image Resizer & Grayscaler 📏")

# File uploader
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    st.subheader("Uploaded Image:")
    st.image(image, caption="Original Image", use_column_width=True)

    # Resize section
    st.subheader("Resize Your Image")
    width = st.number_input("Width (in pixels):", min_value=1, value=image.size[0])
    height = st.number_input("Height (in pixels):", min_value=1, value=image.size[1])

    if st.button("Resize Image"):
        resized_image = image.resize((int(width), int(height)))
        st.image(resized_image, caption="Resized Image", use_column_width=True)

        # Save resized image and add download button
        resized_image.save("resized_image.png")
        with open("resized_image.png", "rb") as file:
            st.download_button(
                label="Download Resized Image",
                data=file,
                file_name="resized_image.png",
                mime="image/png"
            )

    # Grayscale section
    st.subheader("Convert to Grayscale")
    if st.button("Convert to Grayscale"):
        grayscale_image = image.convert("L")
        st.image(grayscale_image, caption="Grayscale Image", use_column_width=True)

        # Save grayscale image and add download button
        grayscale_image.save("grayscale_image.png")
        with open("grayscale_image.png", "rb") as file:
            st.download_button(
                label="Download Grayscale Image",
                data=file,
                file_name="grayscale_image.png",
                mime="image/png"
            )
