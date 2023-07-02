import streamlit as st
import streamlit_chat
from hugchat import hugchat
from hugchat.login import Login

# App title
st.set_page_config(page_title="Buddha Head AI - Find Peace with Us.")

st.title("Buddha Head AI Chat Bot")

# Hugging Face Credentials
with st.sidebar:
    st.title('Buddha Head AI Chatbot')
    st.write("""
    Made by Kunsang T. Ngodup,\n
    for all sentient beings.\n \n 
    \n ☮ Find peace with us. ☮
    """)
    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
        st.success('', icon='✅')
        hf_email = st.secrets['EMAIL']
        hf_pass = st.secrets['PASS']
    else:
        hf_email = st.text_input('Enter E-mail:', type='password')
        hf_pass = st.text_input('Enter password:', type='password')
        if not (hf_email and hf_pass):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')


# Function for generating LLM response

input_container = st.container()
colored_header(label='', description='', color_name='blue-green-90')
response_container = st.container()

def get_text():
    input_text = st.text_input("You: ", "", key="in budhism")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()
sign = Login('BuddhaHead','buddhaheadAI123')
cookies = sign.login()
sign.saveCookies()

def generate_response(prompt_input, email, passwd):
    sign = Login(email, passwd)
    cookies = sign.login()                     
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
