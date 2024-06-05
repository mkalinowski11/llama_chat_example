# import transformers
from flask import Flask
from flask import request
import time
from llama_cpp import Llama
import os

SERVER_PORT = 9501
HOST_URL="127.0.0.1"
MODEL_PATH = os.path.join("..", "models", "capybarahermes-2.5-mistral-7b.Q4_K_M.gguf")
# MODEL_PATH = "./models/vicuna-13b-v1.5.gguf"




def get_model(model_path):
    print("="*100, "\nModel Info\n", "="*100, "\n")
    model = Llama(
        model_path=model_path,
        n_ctx=512,
        n_batch=48
    )
    print("\n", "="*100, "\nModel Info\n", "="*100)
    return model

model = get_model(MODEL_PATH)
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

@app.route("/predict", methods=["POST"])
def predict_response():
    if request.method == "POST":
        data = request.get_json()
        response = generate_response(**data)
        return response

if __name__ == "__main__":
    app.run(host=HOST_URL, port=SERVER_PORT)