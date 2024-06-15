import streamlit as st
import pyrebase
st.set_page_config(page_title="Log in")
# Initialise Firebase Connection
firebase = pyrebase.initialize_app(st.secrets["firebase"])
auth = firebase.auth()
# Once logged in, it will disable the email & password entry fields
is_disabled = False
# Initialise variables for connection
if 'password' not in st.session_state:
    st.session_state["username"] = None
    st.session_state["password"] = None
    st.session_state["is_disabled"] = False
    st.session_state["userToken"] = None

# Title Page
st.title(":rainbow[Log in]")
# Sign Up
def on_login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        verified = auth.get_account_info(user['idToken'])['users'][0].get('emailVerified')
        if verified == False:
            st.warning("Please verify your email before proceeding!")
            st.stop()
        else:
            st.session_state["username"] = email.split('@')[0]
            st.write(f"You are signed in as {email}")
            st.session_state["tracker"] = None
            st.session_state["is_disabled"] = True
            st.session_state['userToken'] = user['idToken']
    except:
        st.warning("Credentials are invalid!")
        st.stop()

if st.session_state["username"] == None:
    email = st.text_input("Email: ", disabled=st.session_state["is_disabled"])
    password = st.text_input("Password: ", type = "password", key = "tracker", disabled=st.session_state["is_disabled"])
    log_in = st.button("Log in!", on_click= on_login, args=(email, password))
else:
    st.write("Username: " , st.session_state["username"])