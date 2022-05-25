FROM python:3.10-alpine

WORKDIR /app
ENV HOME /app

RUN set -ex && unset HISTFILE && \
    apk update && \
    pip install --no-cache-dir pipenv && \
    rm -rf /var/cache/apk/*

COPY Pipfile Pipfile.lock ./

RUN set -ex && \
    pipenv install --system --deploy --ignore-pipfile

COPY ./src ./src
RUN chmod a+x ./src/*
