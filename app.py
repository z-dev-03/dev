import streamlit as st

st.title("DevOps Dashboard")
st.write("Version 1.1 - Simple Update")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! Welcome back ")

st.metric("Builds", "7")     # Changed from 5 to 7
