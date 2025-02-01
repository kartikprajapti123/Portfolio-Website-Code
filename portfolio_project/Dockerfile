FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install psycopg2==2.9.10
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
