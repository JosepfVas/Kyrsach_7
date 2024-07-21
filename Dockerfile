From python:3.12-slim

RUN pip install --upgrade pip && pip install poetry

ENV POETRY_VERSION=1.8.3

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction

COPY . .
