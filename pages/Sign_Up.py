# import module
import streamlit as st

# Setting page title and favicon for window tab
st.set_page_config(page_title="HTS - Sign Up", page_icon="🤖")

# Login form
with st.form("Sign_Up"):
    st.write("Sign Up")
    FirstName = st.text_input("First Name")
    LastName = st.text_input("Last Name")
    username = st.text_input("Username")
    psswd = st.text_input("Password")
    psswdConf = st.text_input("Confirm Password")
    if psswd == psswdConf:
        st.form_submit_button("Login")
st.write("Already have an account?")
st.page_link("pages/Login.py")
