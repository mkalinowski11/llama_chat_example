import streamlit as st
import random
import time
from utils import send_request, response_generator

SERVER_PORT = 9501
HOST_URL="127.0.0.1"
URL = f"http://{HOST_URL}:{SERVER_PORT}/predict"

if __name__ == "__main__":
    
    st.set_page_config(layout="wide")
    st.markdown("<h1 style='text-align: center;'>LLAMA Chat</h1>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    st.sidebar.title("Model parameters")
    st.sidebar.slider(
            "Temperature",
            min_value=0.1,
            max_value=2.,
            value=1.,
            step=0.1,
            key="temperature"
    )
    st.sidebar.slider(
        "Max words",
        min_value=40,
        max_value=512,
        value=128,
        step=2,
        key="max_words"
    )
    st.sidebar.slider(
        "Top p",
        min_value=0.2,
        max_value=0.8,
        value=0.5,
        step=0.1,
        key="top_p"
    )
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                # response_text = st.write_stream(response_generator())
                response = send_request(
                    url=URL,
                    prompt=prompt,
                    max_tokens=st.session_state.max_words,
                    temperature=st.session_state.temperature,
                    top_p=st.session_state.top_p
                )
                response_text = response["choices"][0]["text"].strip()
                st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})