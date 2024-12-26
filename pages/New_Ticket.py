# import module
import streamlit as st

# Setting page title and favicon for window tab
st.set_page_config(page_title='HTS - Create New', page_icon="🤖")
# Sidebar navigation
# Adding a login/sign-up button in side-nav
if st.sidebar.button("Login/Sign up"):
    st.switch_page('pages/Sign_Up.py')
# st.sidebar.page_link('pages/Sign_Up.py', label='Login/Sign Up')
st.sidebar.page_link('streamlit_app.py', label='Home')
st.sidebar.page_link('pages/New_Ticket.py', label='New Ticket')
# Changing width of side nav
st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 14rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 14rem;}}
    </style>
''',unsafe_allow_html=True)

# Setting header with data pulled from the login form to create unique usernames in header
st.title("Welcome {user_ID}!")

# Quick blurb about what to do with a ticket
st.write("Please follow the steps below to describe your issue so I can understand as much as possible. Please "
         "consider saying exactly what you did to get to this issue.")
st.subheader("New Ticket")
col1, col2 = st.columns(2, border=True)
# Dropdown for category selection
with col1:
    issue_type = st.selectbox("What type of category would this ticket fall under?",
                              ("Login Trouble", "General Question", "Setting up technology", "Other"),
                              index=None,
                              placeholder="Please select one of the following:")
    # When the selection made is Other, show textbox for adding more details
    if "Other" == issue_type:
        st.text_input("Please Explain (be generic as this is for categories, "
                      "not to explain your issue in it's entirety.")
description = st.text_input("Description",
                            placeholder="Please tell me what's going on (use as many details as possible)")
with col2:
    # File upload question
    st.file_uploader('Upload file(s)',
                     accept_multiple_files=True)
st.button("Create New Ticket")
