# Pass Dialfire webhook to SugarCRM Call module

[![CircleCI](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM.svg?style=svg)](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)
[![codecov](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM/branch/master/graph/badge.svg)](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)


# Define Environment Variables

    SUGAR_CRM_URL
    SUGAR_CRM_USERNAME
    SUGAR_CRM_PASSWORD 

    SUGAR_CRM_ASSIGNED_USER_ID - optional uuid assigned user
    SUGAR_CRM_WEBHOOK_CONTACT_ID - source contact uuid for passing tests

    no_proxy - list of domain names, to request it without default proxy
    SUGAR_CRM_HOST - define ip of sugar_crm host

    REMOTE - optional, flag to use pass as hash, default False - used plain text pass

    SERVER_HOST - optional public host, default 0.0.0.0
    SERVER_PORT - optional public port, default 8080
    SERVER_DEBUG - optional web server debug mode, default False

# Usage

    Setup in Dialfire webhook to your address:
    http://<address>:8080/webhook

# Install as service 

a)  Docker
    
    setup environment variables in /etc/environment

    cd /opt
    git clone https://github.com/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM dialfire_webhook
    cd dialfire_webhook

    docker build --rm -f "Dockerfile" -t dialfire_webhook:latest .
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
        -e no_proxy \
        --add-host=$(SUGAR_CRM_HOST) \
        dialfire_webhook

b) without Docker
    
    sudo su
    apt-get update
    apt-get install supervisor uwsgi uwsgi-plugin-python -y

    cd /opt
    git clone https://github.com/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM dialfire_webhook
    cd dialfire_webhook

    pip install -r requirements.txt

    cp hook.supervisor.conf /etc/supervisor/conf.d/hook.supervisor.conf

    setup environment variables in /etc/supervisor/conf.d/hook.supervisor.conf

    supervisorctl reload
    supervisorctl restart hook

    to stop service: supervisorctl stop hook
    to start service: supervisorctl start hook
    
 c) Developer server
 
    setup environment variables in /etc/environment

    cd /opt
    git clone https://github.com/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM dialfire_webhook
    cd dialfire_webhook
    pip install -r requirements.txt
    python main.py

# Run test

    > define environment variable SUGAR_CRM_WEBHOOK_CONTACT_ID and run   
    pytest -vs
    
    
