# LLAMA2 Chatbot Example (with contenerized compontents)
This respository provides a code example of using the quantized ```LLAMA 2``` model with the ```llama_cpp``` library, deployed with the Flask framework.
It is intended to run on kubernetes PODs in the future.
Communication between the server and client is established through requests.
The graphical user interface, written in the Streamlit environment,
visualizes the model's responses.

## Requirements
1. Python environment with the following dependencies installed:
    1. llama_cpp_python==0.2.62
    2. streamlit==1.33.0
    3. Flask==3.0.3
    4. requests==2.31.0

2. Downloaded quantized LLAMA 2 model in ```.gguf``` extension from Hugging Face repository.
3. Installed and running docker on the host machine.

The choice of model strictly depends on the application's purpose, and multiple quantized LLAMA models are available. However, manual quantization is also possible. Check out the source 
https://towardsdatascience.com/quantize-llama-models-with-ggml-and-llama-cpp-3612dfbcc172 which clearly
explains the process of quantization of existing model to ```.gguf``` format.

## Project structure explanation
1. `deployment` -> The directory that contains sources for client and server docker containers instances with corresponding dockerfiles to build.
2. `deployment/client/app.py` -> Graphical user interface for communication between client and a server.
It supports LLM parameter modification which are passed within web request to the server.
3. `deployment/server/app_server.py` -> Flask implementation of server providing response in streaming form from the chosen model.
5. `utils.py` -> Some helper methods for server response generation
and prompt processing. This file is duplicated for `client` and `server` directories.
6. `deployment/client/templates` -> Directory with several prompt processing templates available. The choice of the appropriate template depends on the selected model and the training method.

## Running application in Docker environment
### Go to the `deployment/server` directory (1 terminal)
1. Build sufficient docker image by runnning command: `docker build -t llama_chat_server:latest .`
2. Run docker container with command: `docker run -p 0.0.0.0:9502:9502 llama_chat_server:latest`
### Go to the `deployment/client` directory (2 terminal)
1.