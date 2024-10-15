import streamlit as st
import pyrebase
st.set_page_config(page_title="Sign Up")

st.title(":rainbow[Sign Up]")

if 'password' not in st.session_state:
    st.session_state['password'] = None
    st.session_state['gui'] = None


# Initialise the connection
firebase = pyrebase.initialize_app(st.secrets['firebase'])
# Used for authentication part of the application
auth = firebase.auth()

# Function to check email ends with asrjc.edu.sg
def check_email_domain(email):
    return email.endswith("gmail.com")

# Function to check for password requirements
def password_check(password):
    return len(password) > 6

# Sign-Up Function!
def on_signup(email,password):
    try:
        if check_email_domain(email) and password_check(password):
            user = auth.create_user_with_email_and_password(email, password)
            st.session_state['password'] = st.session_state['gui']
            st.session_state['gui'] = ''
            auth.send_email_verification(user['idToken'])
            st.write("Check your email to complete the sign-up!")
        else:
            st.warning("Ensure that you are using your school email!")
    except:
        st.warning("You have signed up before. Contact ICT department for help!")
# Render the Sign Up Page for users which is not logged in.
if st.session_state['username'] is None:
    email = st.text_input("Email for Sign Up: ")
    password = st.text_input("Set a Password: ", type="password", key = 'gui')
    sign_up = st.button("Sign Up!", on_click=on_signup, args= (email,password))
else:
    st.markdown(f"Logged in as {st.session_state['username']}")
