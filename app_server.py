# import transformers
from flask import Flask
from flask import request
import time
from llama_cpp import Llama
import os

SERVER_CONFIG={
    "server_port" : 9501,
    "host_url" : "127.0.0.1",
    "model_path" : os.path.join("..", "models", "codellama-7b-instruct.Q5_K_S.gguf"),
    "model_max_context" : 512
}


def get_model():
    print("="*100, "\nModel Info\n", "="*100, "\n")
    model = Llama(
        model_path=SERVER_CONFIG["model_path"],
        n_ctx=SERVER_CONFIG["model_max_context"],
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

def apply_chat(messages, max_tokens, temperature=0.2, top_p=0.5, stop=["#"], **kwargs):
    response = messages
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

if __name__ == "__main__":
    app.run(host=SERVER_CONFIG["host_url"], port=SERVER_CONFIG["server_port"])