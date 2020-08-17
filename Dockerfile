FROM python:3.8

ENV PYTHONUNBUFFERED=1
LABEL maintainer="Bartosz Gleń"

RUN mkdir /app
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# so that the gettext function works
RUN apt-get update -y && apt-get install -y gettext

RUN useradd user
USER user

EXPOSE 8000

ADD ./friendly_notes ./friendly_notes
