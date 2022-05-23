FROM python:3.10-alpine

RUN set -ex && \
    apk update --no-cache

WORKDIR ./app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile
