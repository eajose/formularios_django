#FROM python:3
#ENV PYTHONUNBUFFERED=1
#RUN mkdir /code
#WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#COPY . /code/

FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential gettext gcc python-dev && apt-get clean

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 8000