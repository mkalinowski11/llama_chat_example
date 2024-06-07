import requests
import random
import time

PROMPT_TOKEN="<PROMPT>"

def read_prompt(path):
    with open(path, "r") as file:
        prompt_lines = file.readlines()
    return "".join(prompt_lines)

def format_prompt(prompt, format_file=None):
    if format_file is None:
        return prompt
    format_text = read_prompt(format_file)
    return format_text.replace(PROMPT_TOKEN, prompt)

def send_request(url, prompt, format_file=None, max_tokens=256, temperature=1.0, top_p=0.5):
    prompt = format_prompt(prompt, format_file=format_file)
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