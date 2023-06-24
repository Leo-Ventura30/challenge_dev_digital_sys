FROM python:3.11.2-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /challenge_dev_digital_sys

COPY requirements.txt /challenge_dev_digital_sys/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /challenge_dev_digital_sys/