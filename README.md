# Pass Dialfire webhook to SugarCRM Call module

[![CircleCI](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM.svg?style=svg)](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)
[![codecov](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM/branch/master/graph/badge.svg)](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)


# Install

Define Environment Variables

    SUGAR_CRM_URL
    SUGAR_CRM_USERNAME
    SUGAR_CRM_PASSWORD 

    SUGAR_CRM_ASSIGNED_USER_ID - optional uuid assigned user
    SUGAR_CRM_WEBHOOK_CONTACT_ID - source contact uuid for passing tests
    
    REMOTE - optional, flag to use pass as hash, default False - used plain text pass

    SERVER_HOST - optional public host, default 0.0.0.0
    SERVER_PORT - optional public port, default 8080
    SERVER_DEBUG - optional web server debug mode, default False

Install requirements
    
    pip install -r requirements.txt

# Run test

    > define environment variable SUGAR_CRM_WEBHOOK_CONTACT_ID and run   
    pytest -vs

# Run server dev server
    
    ./main.py

# Run docker container

    > build

    docker build --rm -f "Dockerfile" -t dialfire_webhook:latest .

    > run 

    export SUGAR_CRM_URL=http://......./service/v4_1/rest.php
    export SUGAR_CRM_USERNAME=.......
    export SUGAR_CRM_PASSWORD='.......'
    export SUGAR_CRM_ASSIGNED_USER_ID='.......'

    docker run \
        -it \
        --rm \
        -p 8080:8080 \
        -e SUGAR_CRM_URL \
        -e SUGAR_CRM_USERNAME \
        -e SUGAR_CRM_PASSWORD \
        -e SUGAR_CRM_ASSIGNED_USER_ID \
        -e SERVER_DEBUG \
        -e REMOTE \
        dialfire_webhook

    > open http://127.0.0.1:8080
    