# Pass Dialfire webhook to SugarCRM Call module

[![CircleCI](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM.svg?style=svg)](https://circleci.com/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)
[![codecov](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM/branch/master/graph/badge.svg)](https://codecov.io/gh/AlekseyMolchanov/Pass_Dialfire_webhook_to_SugarCRM)


# Install

Define Environment Variables

    SERVER_HOST - public host
    SERVER_PORT - public port
    SERVER_DEBUG - optional web server debug mode

    SUGAR_CRM_URL
    SUGAR_CRM_USERNAME
    SUGAR_CRM_PASSWORD 

    SUGAR_CRM_ASSIGNED_USER_ID - optional uuid assigned user

    SUGAR_CRM_WEBHOOK_TASK_ID - source task uuid for passing tests

Install requirements
    
    pip install -r requirements.txt

# Run test

    > define environment variable SUGAR_CRM_WEBHOOK_TASK_ID and run   
    pytest -vs

# Run server
    
    ./main.py

