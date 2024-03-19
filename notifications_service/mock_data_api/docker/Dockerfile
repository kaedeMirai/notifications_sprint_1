FROM python:3.11

WORKDIR /app
ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry

COPY ./Makefile Makefile
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN poetry config virtualenvs.create false \
    && poetry install --no-cache --no-root

COPY ./notifications_service/mock_data_api/docker/docker-entrypoint.sh ./docker-entrypoint.sh

COPY ./notifications_service/mock_data_api/src ./

RUN chmod o+x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]