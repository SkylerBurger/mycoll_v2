FROM python:3.9.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN apt-get -y update
RUN apt-get -y install git
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

COPY . /code/