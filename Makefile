POETRY = ./.venv/bin/poetry


venv:
	@rm -rf .venv || true && \
	python3.11 -m venv .venv && \
	.venv/bin/pip install poetry && \
	${POETRY} install --no-root

run:
	docker compose -f docker-compose.yaml up -d

stop:
	docker compose -f docker-compose.yaml down -v

api_build:
	docker build -t api_service -f ./notifications_service/api_service/docker/Dockerfile .

mock_data_api_build:
	docker build -t mock_data_api_service -f ./notifications_service/mock_data_api/docker/Dockerfile .

worker_build:
	docker build -t worker_sender -f ./notifications_service/worker/docker/Dockerfile .

run_with_uvicorn:
	uvicorn main:app --log-level=debug --host=0.0.0.0 --port=8000

run_mock_data_api_with_uvicorn:
	uvicorn main:app --log-level=debug --host=0.0.0.0 --port=8000