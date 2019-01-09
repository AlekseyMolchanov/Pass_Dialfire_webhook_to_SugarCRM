test:
	pytest -vs

build:
	docker build --rm -f "Dockerfile" -t dialfire_webhook:latest .

clear_build:
	docker build --no-cache --rm -f "Dockerfile" -t dialfire_webhook:latest .
	
