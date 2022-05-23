FROM python:3.10-alpine

ARG BUILD_PKG=""
ARG BUILD_DEPS=""

WORKDIR /app
ENV HOME /app

RUN set -ex && \
    apk --update add --no-cache $BUILD_PKG && \
    pip install pipenv --no-cache-dir && \
    rm -rf /var/cache/apk/*

COPY Pipfile Pipfile.lock ./

RUN set -ex && \
    apk add --no-cache --virtual build_deps $BUILD_DEPS && \
    pipenv install --system --deploy --ignore-pipfile && \
    rm -rf /var/cache/apk/* && \
    apk del build_deps

COPY ./src .
