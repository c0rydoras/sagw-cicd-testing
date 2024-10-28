FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
  POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi


COPY . .

EXPOSE 8000

CMD  ["fastapi", "run", "./example/main.py"]
