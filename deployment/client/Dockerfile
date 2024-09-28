FROM python:3.10.14-slim

COPY ./requirements.txt /app/requirements.txt
COPY ./templates/template1.txt /app/templates/template1.txt
COPY ./templates/template2.txt /app/templates/template2.txt
COPY ./templates/template3.txt /app/templates/template3.txt
COPY ./utils.py /app/utils.py
COPY ./app.py /app/app.py

WORKDIR /app

RUN apt-get update -y \
    && apt-get install gcc g++ cmake libc-dev -y

RUN pip3 install -r requirements.txt

ENV HOST_URL=0.0.0.0
ENV SERVER_PORT=9502
ENV URL=http://0.0.0.0:9502/predict_stream
ENV TEMPLATE_PATH=./templates/template2.txt

EXPOSE 9503

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=9503", "--server.address=0.0.0.0"]