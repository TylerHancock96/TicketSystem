# import module
import streamlit as st

# Setting page title and favicon for window tab
st.set_page_config(page_title="HTS - Main Page", page_icon="🤖")
# header
st.header("What is this?")

# Create new ticket button
st.page_link("pages/New_Ticket.py", label="Create a new ticket")
