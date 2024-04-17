import streamlit as st
from PIL import Image
from RAGChapter1 import answer
# Each Python file in the pages folder represents a chapter
st.title(":rainbow[Chapter 1]")
# Create a row with 3 columns to evenly space the buttons
col1, col2, col3 = st.columns(3)
# Inside each of the column you can choose how many buttons you want to add
with col1:
    b1 = st.button("Button 1")
with col2:
    b2 = st.button("Button 2")
with col3:
    b3 = st.button("Button 3")
# To show different content when each button is pressed:
if b1:
    st.write("**Button 1 is pressed**")
    python_logo = Image.open("./images/Chapter1/python.png")
if b2:
    st.write("**Button 2 is pressed**")
if b3:
    st.write("**Button 3 is pressed**")
# Adding the chatbot functionality
st.divider()
# Create a temporary list to store messages until user refresh
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
# Show all the messages previously sent
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
# Create a chat input field for user to key in answers
chat_box = st.chat_input("Enter your question here: ")
if chat_box:
    with st.chat_message('user'):
        st.markdown(chat_box)
        st.session_state['messages'].append({'role': 'user', 'content': chat_box})
    with st.chat_message('assistant'):
        response = answer(chat_box)
        st.markdown(response)
        st.session_state['messages'].append({'role': 'assistant', 'content': response})