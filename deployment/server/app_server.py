# import transformers
from flask import Flask, Response, request
import time
from llama_cpp import Llama
import os
from utils import response_stream_generator

# default default_config should correspond to the original one from parent directory
default_config = {
    "server_port" : 9502,
    "host_url" : "127.0.0.1",
    "url" : "http://127.0.0.1:9502/predict_stream",
    "template_path" : "./templates/template2.txt",
    "model_path" : "../models/codellama-7b-instruct.Q5_K_S.gguf",
    "model_max_context" : 512
}

def get_model():
    print("="*100, "\nModel Info\n", "="*100, "\n")
    model = Llama(
        model_path=os.environ.get("MODEL_PATH", default_config["model_path"]),
        n_ctx=int(os.environ.get("MODEL_MAX_CONTEXT", default_config["model_max_context"])),
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
    app.run(
        host=os.environ.get("HOST_URL", default_config["host_url"]),
        port=int(os.environ.get("SERVER_PORT", default_config["server_port"]))
    )