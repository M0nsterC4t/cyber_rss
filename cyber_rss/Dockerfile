FROM python:3.11.8-slim

WORKDIR /cyber_rss

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt


COPY . .

COPY .env.prod .env

CMD python main.py