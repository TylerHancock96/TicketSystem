# import module
import streamlit as st
# Setting page title and favicon for window tab
st.set_page_config(page_title="HTS - Sign Up", page_icon="🤖")
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
