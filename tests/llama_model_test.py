from llama_cpp import Llama
import os
# https://llama-cpp-python.readthedocs.io/en/latest/api-reference/?ref=localhost#llama_cpp.Llama
# https://awinml.github.io/llm-ggml-python/

system_message = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

def format_prompt(prompt):
    return """<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant"""
# for testing used models from: https://medium.com/@ingridwickstevens/quantization-of-llms-with-llama-cpp-9bbf59deda35

if __name__ == "__main__":
    model_path = os.path.join("..", "..", "models", "nous-hermes-2-mistral-7B--Q5_K_M.gguf")
    llama_model = Llama(
        model_path=model_path, n_ctx=512, n_batch=48, verbose=False
    )
    prompt = "Why the earth is movind arozund the sun?"
    formatted_prompt = format_prompt(prompt)
    formatted_prompt = prompt
    max_tokens = 128
    response = llama_model(
        formatted_prompt,
        max_tokens=max_tokens,
        temperature=0.4,
        top_p=0.5,
        echo=False,
        stop=["#"]
    )
    # print("### Input prompt")
    # print(prompt)
    print("### Response from regular text generation")
    print(response["choices"][0]["text"])
    print("Generator response", "="*100)

    def generate(llama_model, prompt, max_len=128, **kwargs):
        tokenized_prompt = llama_model.tokenize(str.encode(prompt))
        for idx, token in enumerate(llama_model.generate(tokenized_prompt, **kwargs)):
            if token == llama_model.token_eos() or idx == max_len:
                break
            yield llama_model.detokenize([token]).decode()

    # print("model stop token", llama_model.token_eos(), llama_model.detokenize([llama_model.token_eos()]))
    generated_text = "".join([token for token in generate(llama_model, formatted_prompt, max_len=256, top_p=0.5, temp=0.9, repeat_penalty=1.5)])
    print(generated_text)