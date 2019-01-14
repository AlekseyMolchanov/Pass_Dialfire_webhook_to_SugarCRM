# Pass Dialfire webhook to SugarCRM Call module

[![CircleCI](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM.svg?style=svg)](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)
[![codecov](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM/branch/master/graph/badge.svg)](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)


# Define Environment Variables

    To define Environment Variables
    You can add to /etc/environment
    and run : source /etc/environment
    or reboot server

    example:

        export SUGAR_CRM_URL=http://...../service/v4_1/rest.php
        export SUGAR_CRM_USERNAME='username'
        export SUGAR_CRM_PASSWORD='password'
        export no_proxy='127.0.0.1, crm.local'
      

    required:

    SUGAR_CRM_URL
    SUGAR_CRM_USERNAME
    SUGAR_CRM_PASSWORD 

    optional:

    SUGAR_CRM_ASSIGNED_USER_ID - user_id assigned user
    no_proxy - list of domain names, to request it without default proxy
    SUGAR_CRM_HOST - define ip of sugar_crm host

    REMOTE - flag to use pass as hash, default False - used plain text pass
    
    SERVER_HOST - public host, default 0.0.0.0
    SERVER_PORT - public port, default 8080
    SERVER_DEBUG - web server debug mode, default False

    for testing:

    SUGAR_CRM_WEBHOOK_CONTACT_ID - source contact uuid for passing tests

# Usage

    After run service or console command you can open 
    http://127.0.0.1:8080

    To use dbsync with webhook service runed on interface 127.0.0.1
    you must add to docker-compose file option:
    
    network_mode: "host"

    resource to accept dbsync callback : http://127.0.0.1:8080/webhook


# Run as console process (not recommended for production)

    * setup Environment Variables
    
    cd /opt
    git clone https://github.com/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM dialfire_webhook
    cd dialfire_webhook
    pip install -r requirements.txt
    python main.py
    

# Run as servise without Docker (recommended for production)

    sudo su
    apt-get update
    apt-get install supervisor uwsgi uwsgi-plugin-python -y

    cd /opt
    git clone https://github.com/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM dialfire_webhook
    cd dialfire_webhook
    pip install -r requirements.txt
    cp hook.supervisor.conf /etc/supervisor/conf.d/hook.supervisor.conf

    * setup environment variables in /etc/supervisor/conf.d/hook.supervisor.conf

    supervisorctl reload
    supervisorctl restart hook

    to stop service: supervisorctl stop hook
    to start service: supervisorctl start hook

    *To run as console proces.
    Exec after setup environment variables in the console command:*
    
        uwsgi \
            --master \
            --plugin python \
            --http-socket 127.0.0.1:8080 \
            --processes 5 \
            --chdir /opt/dialfire_webhook \
            --module wsgi:app \
            --logto=/tmp/uwsgi.hook.log


# Run as servise with Docker (recommended for production)

    sudo su
    apt-get update
    apt-get install docker
    
    * setup environment variables in /etc/environment

    make build
    make run_docker_service

    *To run as console proces.
    Exec after building in the console command:*
    
        make run_docker
        or
        docker run \
            -it \
            --rm \
            -p 8080:8080 \
            -e SUGAR_CRM_URL \
            -e SUGAR_CRM_USERNAME \
            -e SUGAR_CRM_PASSWORD \
            -e SUGAR_CRM_ASSIGNED_USER_ID \
            -e SERVER_DEBUG \
            -e no_proxy \
            --add-host=$SUGAR_CRM_HOST \
            dialfire_webhook


# Run test

    * setup Environment Variables
    ** define environment variable SUGAR_CRM_WEBHOOK_CONTACT_ID

    cd /opt
    git clone https://github.com/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM dialfire_webhook
    cd dialfire_webhook
    pip install -r requirements.txt

    pytest -vs