######################IMPORTS####################
import openai
from langchain.llms import OpenAI

import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
llm=OpenAI(temperature=0)


######################IMPORTS####################

#######################MAIN######################

st.title("Buddha Head")
openai.api_key = st.secrets["OPENAI_API_KEY"]


#######################MAIN######################

######################SIDEBAR####################

with st.sidebar:
    st.title('Introduction and Information')
    st.markdown("""🙏Buddha Head is an AI 
    chatbot designed for you to engage in 
    meaningful conversations with and explore 
    the teachings of Buddhism with this virtual 
    companion, empowering you to find inner 
    peace and harmony.""")
    st.markdown("Please feel free to ask any questions you may have. Remember, the path to enlightenment is a journey we're all on together.")
    add_vertical_space(11)
    st.write("""
    Made by Kunsang T. Ngodup.\n
    For all sentient beings.\n \n 
    \n ☮ Find peace with us. ☮
    """)
    add_vertical_space(1)
    st.write("If you are in an actual life-threatening situation call +1 (833)-456-4566.")
    
######################SIDEBAR####################

####################ACTUAL CODE##################

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What Would you like to learn about today"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

for response in openai.ChatCompletion.create(model=st.session_state["openai_model"], messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages], stream=True): 
    full_response += response.choices[0].delta.get("content", ""),message_placeholder.markdown(full_response + "▌"), message_placeholder.markdown(full_response)
st.session_state.messages.append({"role": "assistant", "content": full_response})