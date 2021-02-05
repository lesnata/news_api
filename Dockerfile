FROM python:3.7-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
MAINTAINER My Project
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /news-api
COPY . /news-api

RUN adduser -D user
USER user

CMD python manage.py runserver 0.0.0.0:$PORT