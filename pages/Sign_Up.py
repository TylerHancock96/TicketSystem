# import module
import streamlit as st

# Setting page title and favicon for window tab
st.set_page_config(page_title="HTS - Sign-Up", page_icon="🤖")

# Login form
with st.form("Login_Sign_Up"):
    st.write("Login")
    username = st.text_input("Username")
    psswd = st.text_input("Password")
    st.form_submit_button("Login")
