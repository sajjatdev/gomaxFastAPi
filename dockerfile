FROM python:3-alpine3.15

WORKDIR /app

COPY . /app

EXPOSE 8000

RUN pip install -r requirements.txt
