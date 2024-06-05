import streamlit as st
import random
import time
import requests

SERVER_PORT = 9501
HOST_URL="127.0.0.1"
URL = f"http://{HOST_URL}:{SERVER_PORT}/predict"

def format_prompt(prompt):
    return f"""<|im_start|>system
You are a helpful chatbot.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>"""

def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    time.sleep(2.)
    for word in response.split():
        yield word + " "
        time.sleep(.5)

def send_request(prompt):
    prompt = format_prompt(prompt)
    data = {
        "prompt": prompt,
        "max_tokens": 256,
        "temperature": 0.4,
        "top_p": 0.5
    }
    response = requests.post(URL, json=data)
    return response.json()

st.title("LLAMA chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            # response = st.write_stream(response_generator())
            response = send_request(prompt)
            response_text = response["choices"][0]["text"].strip()
            st.markdown(response_text)
    st.session_state.messages.append({"role": "assistant", "content": response_text})