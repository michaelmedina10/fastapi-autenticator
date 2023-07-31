build:
	docker build . -t fastapi_app

run:
	docker run -p8000:8000 --name fastapi_app fastapi_app

bash:
	docker exec -it fastapi_app /bin/bash

remove:
	docker rm -f fastapi_app

executar:
	make remove || true
	make build
	make run
env:
	python3 -m venv venv

test:
	python3 -m pytest -s -vv --cov=iga_watchmen_sonda_prometheus --cov-report=term-missing
