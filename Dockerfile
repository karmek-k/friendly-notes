FROM python:3.8

ENV PYTHONUNBUFFERED=1
LABEL maintainer="Bartosz Gleń"

RUN mkdir /app
WORKDIR /app

EXPOSE 8000

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# so that the gettext function works
RUN apt-get update -y && apt-get install -y gettext

ADD ./friendly_notes ./friendly_notes
