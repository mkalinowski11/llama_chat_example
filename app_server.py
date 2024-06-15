# import transformers
from flask import Flask, Response, request
import time
from llama_cpp import Llama
import os
from utils import response_stream_generator, read_config

config = read_config("./config.json")

def get_model():
    print("="*100, "\nModel Info\n", "="*100, "\n")
    model = Llama(
        model_path=config["model_path"],
        n_ctx=config["model_max_context"],
        n_batch=48
    )
    print("\n", "="*100, "\nModel Info\n", "="*100)
    return model

model = get_model()
app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Test server!</p>"

def generate_response(prompt, max_tokens=512, temperature=0.2, top_p=0.5, stop=["#"], **kwargs):
    response = model(
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        stop=stop,
        **kwargs
    )
    return response

def apply_chat(messages, max_tokens, temp=0.2, top_p=0.5, stop=["#"], **kwargs):
    response = model.create_chat_completion(
        messages,
        max_tokens=max_tokens,
        temperature=temp,
        top_p=top_p,
        stop=stop,
        **kwargs
    )
    return response

@app.route("/predict", methods=["POST"])
def predict_response():
    if request.method == "POST":
        data = request.get_json()
        response = generate_response(**data)
        return response

@app.route("/predict_chat", methods=["POST"])
def predict_chat():
    if request.method == "POST":
        data = request.get_json()
        response = apply_chat(**data)
        return response

@app.route("/predict_stream", methods=["POST"])
def predict_stream():
    if request.method == 'POST':
        data = request.get_json()
        return Response(response_stream_generator(model, **data), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(host=config["host_url"], port=config["server_port"])