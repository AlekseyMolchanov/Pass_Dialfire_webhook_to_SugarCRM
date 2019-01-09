#!/usr/bin/env python
# encoding: utf-8

from json import dumps
from flask import Flask, request
from sugarcrm import Call

from processor import process
from connection import sugar_crm_connect, server_settings

session = sugar_crm_connect()
if not session:
    print("\n######## Warning ########")
    print("You must define Environment Variables:")
    print("SUGAR_CRM_URL, SUGAR_CRM_USERNAME and SUGAR_CRM_PASSWORD")
    print("###########################\n")
    exit(1)

settings = server_settings()
if not settings:
    print("\n######## Warning ########")
    print("You must define Environment Variables:")
    print("SERVER_HOST, SERVER_PORT")
    print("\n######## Optional ########")
    print("SERVER_DEBUG, SUGAR_CRM_ASSIGNED_USER_ID")
    print("###########################\n")
    exit(1)

app = Flask(__name__)

@app.route('/')
def webhook_index():
    return 'index'

@app.route('/webhook', methods=['POST'])
def webhook_post():
    params = request.get_json(force=True)
    call_id, data = process(session, params)
    return dumps(data)


if __name__ == "__main__":
    app.run(**settings)
