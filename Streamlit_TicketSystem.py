# import module
import streamlit as st

# title
st.title("Hjelmar Ticketing System")

# header
st.header("What is this?")

# Explanation
st.write("This is a system I created for friends and family to send me any IT/computer issues without the need to "
         "call me. My plan is to sift through the tickets as they come in and prioritize them based on level of "
         "severity.")

# Get started button that will open login/sign-up page
if st.button("Let's get started"):
    with st.form("Login_Sign_Up"):
        st.write("Login")
        username = st.text_input("Username")
        psswd = st.text_input("Password")
        st.form_submit_button("Login")
    st.page_link("Sign Up")
