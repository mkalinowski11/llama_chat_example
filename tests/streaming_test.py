import requests
import os
import sys
sys.path.append("../")
from utils import format_prompt, byte_str_adapter

prompt_file = os.path.join(
    "..", "templates", "template2.txt"
)
prompt = "Why is an earth moving around the sun"

port = 9502
url = f"http://127.0.0.1:{port}/predict_stream"
data = {
    "prompt" : format_prompt(prompt, format_file=prompt_file),
    "max_tokens": 128,
    "temp" : 1.0,
    "top_p": 0.3
}

# sending a request and fetching a response which is stored in r
# with requests.post(url, json=data, stream=True) as r:
#     # printing response of each stream
#     for chunk in r.iter_content(1024):
#         print(chunk.decode())

response = byte_str_adapter(requests.post(url, json=data, stream=True))
for token in response:
    print(token)