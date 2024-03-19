FROM python:3.11

WORKDIR /app
ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry

COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN poetry config virtualenvs.create false \
    && poetry install --no-cache --no-root

COPY . .

COPY notifications_service/worker/docker/wait-for-it.sh .
RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "rabbitmq", "5672", "--", "python", "src/main.py"]
