import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Sine Wave Generator 🌊")

# User input for sine wave parameters
st.sidebar.header("Customize Your Sine Wave")
amplitude = st.sidebar.slider("Amplitude", 1, 10, 1)
frequency = st.sidebar.slider("Frequency (Hz)", 1, 10, 1)
phase = st.sidebar.slider("Phase (radians)", 0.0, 2.0 * np.pi, 0.0, step=0.1)
x_limit = st.sidebar.slider("X-axis Limit", 1, 20, 10)

# Generate the sine wave
x = np.linspace(0, x_limit, 1000)
y = amplitude * np.sin(2 * np.pi * frequency * x + phase)

# Plot the sine wave
st.header("Sine Wave Plot")
fig, ax = plt.subplots()
ax.plot(x, y, label=f"Sine Wave: A={amplitude}, f={frequency}Hz, ϕ={round(phase, 2)} rad")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.legend()
ax.grid(True)

# Display the plot in the app
st.pyplot(fig)

# Show the wave equation
st.subheader("Wave Equation:")
st.latex(r"y = A \sin(2\pi f x + \phi)")
st.write(f"A = {amplitude}, f = {frequency}Hz, ϕ = {round(phase, 2)} rad")