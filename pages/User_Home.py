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

# Create new ticket button
st.page_link("pages/New_Ticket.py", label="Create a new ticket")
