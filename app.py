import streamlit as st

st.title("Simple DevOps Dashboard")
st.write("This is version 1.0")

name = st.text_input("Your name here")
if name:
    st.success(f"Hello, {name}!")

st.metric("Builds", "5")