# import module
import streamlit as st

# Setting page title and favicon for window tab
st.set_page_config(page_title="HTS - Main Page", page_icon="🤖")

# title
st.title("Hjelmar Ticketing System")

# Adding a login/sign-up button in side-nav
with st.sidebar:
    sideb = st.sidebar
    signlog = sideb.button("Login/Sign Up")
    if signlog:
        st.page_link("pages/Login.py")
        st.page_link("pages/Sign_Up.py")
# header
st.header("What is this?")

# Explanation
st.write("This is a system I created for friends and family to send me any IT/computer issues without the need to "
         "call me. My plan is to sift through the tickets as they come in and prioritize them based on level of "
         "severity.")
