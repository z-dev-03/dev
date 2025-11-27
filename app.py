import streamlit as st

st.title("DevOps Dashboard v1.2")

page = st.sidebar.selectbox("Select:", ["Home", "Settings"])

if page == "Home":
    st.write("Simple update with enhanced greeting")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! Welcome back")
    st.metric("Builds", "7")
else:
    st.subheader("Settings")
    st.write("Configure your dashboard preferences here")
