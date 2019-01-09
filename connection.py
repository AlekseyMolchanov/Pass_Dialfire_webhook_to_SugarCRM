#!/usr/bin/env python
# encoding: utf-8

import os
from sugarcrm import Session


def sugar_crm_connect():
    session = None
    try:
        auth=Session.local_auth

        if os.environ.get('CIRCLECI'):
            auth=Session.remote_auth

        url = os.environ['SUGAR_CRM_URL']
        username = os.environ['SUGAR_CRM_USERNAME']
        password = os.environ['SUGAR_CRM_PASSWORD']
        session = Session(url, username, password, auth=auth)
    except KeyError as exception:
        pass
    return session


def server_settings():
    _connect = dict()
    try:
        host = os.environ['SERVER_HOST']
        port = os.environ['SERVER_PORT']
        debug = bool(int(os.environ.get('SERVER_DEBUG') or 0))
        _connect = dict(
            debug=debug, 
            host=host, 
            port=port
        )
    except KeyError as exception:
        pass
    return _connect    
   