import requests
import json

SERVER_PORT = 9501
HOST_URL="127.0.0.1"
URL = f"http://{HOST_URL}:{SERVER_PORT}/predict"

def format_prompt(prompt):
    return f"""<|im_start|>system
You are a helpful chatbot.<|im_end|>
<|im_start|>user 
{prompt}<|im_end|>"""

def send_request(prompt):
    # prompt=format_prompt(prompt)
    data={
        "prompt": prompt,
        "max_tokens": 128,
        "temperature": 0.4,
        "top_p": 0.5
    }
    return requests.post(URL, json=data)

if __name__ == "__main__":
    prompt = "Why the earth is movind around the sun"
    print("provided prompt ::", prompt)
    response = send_request(prompt)
    response = response.json()
    print("got response ::")
    print(response)