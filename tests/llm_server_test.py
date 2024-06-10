import sys
sys.path.append("../")
from utils import send_request

SERVER_PORT = 9502
HOST_URL="127.0.0.1"
# URL = f"http://{HOST_URL}:{SERVER_PORT}/predict"
URL = f"http://{HOST_URL}:{SERVER_PORT}/predict_chat"


if __name__ == "__main__":
    # prompt = "Why the earth is movind around the sun"
    # prompt = "Write a function that returns a list comprehension with even numbers only with range from 0 to 101, with explanation"
    # print("provided prompt ::", prompt)
    messages = [
        {"role" : "user", "content" : "hi, I like being scared, what type of film do you recommend me to watch"},
        {"role" : "assistant", "content" : "hello, I definitely recommend watching horror fils. Here is an example of a film worth to consider, the bloody pillar."},
    ]
    # response = send_request(URL, messages).json()
    # message = response["choices"][0]["message"]["content"]
    messages.extend([
        {"role" : "user", "content" : "what is my preference from the first question and what title of film you have recommended mi to watch?"}
    ])
    response = send_request(URL, messages)
    data = response.json()
    print(data)