FROM python:3.8

ENV PYTHONUNBUFFERED=1
LABEL maintainer="Bartosz Gleń"

RUN mkdir /app
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD . .

RUN useradd user
USER user
