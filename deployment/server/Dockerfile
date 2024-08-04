FROM python:3.10.14-slim

COPY ./requirements.txt /app/requirements.txt
COPY ./models/codellama-7b-instruct.Q5_K_S.gguf /app/models/codellama-7b-instruct.Q5_K_S.gguf
COPY ./utils.py /app/utils.py
COPY ./app_server.py /app/app_server.py

WORKDIR /app

RUN pip install -r requirements.txt

RUN export MODEL_PATH=./models/codellama-7b-instruct.Q5_K_S.gguf
RUN export HOST_URL=127.0.0.1
RUN export SERVER_PORT=9502
RUN export MODEL_MAX_CONTEXT=512

ENTRYPOINT ["python"]
CMD ["app_server.py"]