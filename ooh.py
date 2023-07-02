import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="Buddha Head AI - Find Peace with Us.")
st.title("Buddha Head AI Chat Bot")
with st.sidebar:
    st.title("Buddha Head AI Chatbot")
    st.write("""
    Made by Kunsang T. Ngodup,\n
    for all sentient beings.\n \n 
    \n ☮ Find peace with us. ☮
    """)
    add_vertical_space(5)
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["""Greetings, seeker. I am Buddha Head. I am here to help you overcome obstacles. May the power of love, compassion, and wisdom guide you.\nPlease feel free to ask any questions you may have. Remember, the path to enlightenment is a journey we're all on together."""]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='green-70')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="in budhism")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt="in Buddhism")
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

