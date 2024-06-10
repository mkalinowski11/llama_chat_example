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

def send_request(url, prompt, format_file=None, max_tokens=256, temperature=1.0, top_p=0.5, **kwargs):
    data = {}
    if isinstance(prompt, str):
        prompt = format_prompt(prompt, format_file=format_file)
        data["prompt"] = prompt
    elif isinstance(prompt, list):
        data["messages"] = prompt
    data.update({
        "max_tokens": max_tokens,
        # "temperature": temperature,
        "temp" : temperature,
        "top_p": top_p
    })
    response = requests.post(url, json=data, stream=True)
    # return response.json()
    return response

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

def response_stream_generator(llama_model, prompt, max_tokens=128, **kwargs):
    tokenized_prompt = llama_model.tokenize(str.encode(prompt))
    for idx, token in enumerate(llama_model.generate(tokenized_prompt, **kwargs)):
        if token == llama_model.token_eos() or idx == max_tokens:
            break
        yield llama_model.detokenize([token])

def byte_str_adapter(input_generator):
    for token in input_generator:
        yield token.decode()