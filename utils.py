import requests
import random
import time

PROMPT_TOKEN="<PROMPT>"
PROMPT_TYPE="codelllama"
PROMPT_FORMATS = {
    "universal": """<|im_start|>system\nYou are a helpful chatbot.<|im_end|>\n<|im_start|>user\n<PROMPT><|im_end|>""",
    "codelllama": """[INST] Write code to solve the following coding problem that obeys the constraints and passes the example test cases. Please wrap your code answer using ```:\n<PROMPT>\n[/INST]"""
}

def read_prompt(path):
    with open(path, "r") as file:
        prompt_lines = file.readlines()
    return "".join(prompt_lines)

def format_prompt(prompt, prompt_type="universal"):
    if prompt_type is None:
        return prompt
    return PROMPT_FORMATS[prompt_type].replace(PROMPT_TOKEN, prompt)

def send_request(url, prompt, max_tokens=256, temperature=1.0, top_p=0.5):
    prompt = format_prompt(prompt, prompt_type=PROMPT_TYPE)
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