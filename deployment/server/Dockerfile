FROM python:3.10.14-slim

COPY ./requirements.txt /app/requirements.txt
COPY ./models/codellama-7b-instruct.Q5_K_S.gguf /app/models/codellama-7b-instruct.Q5_K_S.gguf
COPY ./utils.py /app/utils.py
COPY ./app_server.py /app/app_server.py

WORKDIR /app

RUN apt-get update -y \
    && apt-get install gcc g++ cmake libc-dev -y

RUN pip3 install -r requirements.txt

ENV MODEL_PATH=./models/codellama-7b-instruct.Q5_K_S.gguf
ENV HOST_URL=0.0.0.0
ENV SERVER_PORT=9502
ENV MODEL_MAX_CONTEXT=512

ENTRYPOINT ["python"]
CMD ["app_server.py"]