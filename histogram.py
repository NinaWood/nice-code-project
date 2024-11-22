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