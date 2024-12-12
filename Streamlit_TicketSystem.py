# import module
import streamlit as st

# Setting page title and favicon for window tab
st.set_page_config(page_title="HTS - Main Page", page_icon="🤖")

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
    st.page_link("pages/Login_Page.py")
