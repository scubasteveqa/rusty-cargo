import ctypes
import os
import streamlit as st

# Load the Rust shared library
if os.name == "nt":  # Windows
    rust_lib = ctypes.CDLL("./target/release/rust_library.dll")
else:  # Linux/Mac
    rust_lib = ctypes.CDLL("./target/release/librust_library.so")

# Define the Rust function signature
rust_lib.square.argtypes = [ctypes.c_double]
rust_lib.square.restype = ctypes.c_double

# Streamlit app
st.title("Rust + Streamlit Without Maturin")
st.write("This app uses a Rust shared library to calculate the square of a number.")

# Input
number = st.number_input("Enter a number to square:", value=1.0, step=0.1)

# Call Rust function and display result
if st.button("Calculate Square"):
    result = rust_lib.square(number)
    st.success(f"The square of {number} is {result}")
