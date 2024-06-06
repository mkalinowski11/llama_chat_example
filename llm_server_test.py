import requests
import json
from utils import format_prompt

SERVER_PORT = 9501
HOST_URL="127.0.0.1"
URL = f"http://{HOST_URL}:{SERVER_PORT}/predict"

def send_request(prompt):
    prompt=format_prompt(prompt, prompt_type="codelllama")
    # prompt=format_prompt(prompt)
    print(f"formatted prompt :: {prompt}")
    data={
        "prompt": prompt,
        "max_tokens": 128,
        "temperature": 0.4,
        "top_p": 0.5
    }
    return requests.post(URL, json=data)

if __name__ == "__main__":
    # prompt = "Why the earth is movind around the sun"
    prompt = "Write a function that returns a list comprehension with even numbers only with range from 0 to 101, with explanation"
    print("provided prompt ::", prompt)
    response = send_request(prompt)
    response = response.json()
    print("got response ::")
    print(response)