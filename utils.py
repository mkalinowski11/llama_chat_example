import requests
import random
import time

def format_prompt(prompt):
    return f"""<|im_start|>system
You are a helpful chatbot.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>"""

def send_request(url, prompt, max_tokens=256, temperature=1.0, top_p=0.5):
    prompt = format_prompt(prompt)
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p
    }
    response = requests.post(url, json=data)
    return response.json()

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