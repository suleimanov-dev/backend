FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN pip install poetry==1.1.12
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
