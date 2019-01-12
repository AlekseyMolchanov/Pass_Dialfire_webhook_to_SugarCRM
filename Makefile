test:
	pytest -vs

build:
	docker build --rm -f "Dockerfile" -t dialfire_webhook:latest .

clear_build:
	docker build --no-cache --rm -f "Dockerfile" -t dialfire_webhook:latest .
	
run_docker:

	docker run \
        -it \
        --rm \
        -p 8080:8080 \
        -e SUGAR_CRM_URL \
        -e SUGAR_CRM_USERNAME \
        -e SUGAR_CRM_PASSWORD \
        -e SUGAR_CRM_ASSIGNED_USER_ID \
        -e NO_PROXY \
        --add-host='bestcrm.bechtle.intra:10.252.11.10' \
        dialfire_webhook
