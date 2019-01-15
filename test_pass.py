#!/usr/bin/env python
# encoding: utf-8

import os
import pytest
from sugarcrm import Call, Contact
from connection import sugar_crm_connect, server_settings
from processor import process

from const import FIELDS

CONTACT_ID = os.environ['SUGAR_CRM_WEBHOOK_CONTACT_ID']

@pytest.fixture(scope="module")
def session():
    session = sugar_crm_connect()
    return session


@pytest.fixture(scope="module")
def state():
    __state = {'account': None}
    return __state


def test_env(session, state):
    assert os.environ.get('SUGAR_CRM_URL')
    assert os.environ.get('SUGAR_CRM_USERNAME')
    assert os.environ.get('SUGAR_CRM_PASSWORD')
    assert os.environ.get('SUGAR_CRM_ASSIGNED_USER_ID')


def test_source_contact(session, state):
    contact = session.get_entry(Contact.module, CONTACT_ID)
    assert contact


def test_invalid_input1(session, state):

    input_data = {
        "contact": {
            "$ref": 'xxxx-xxxx-xxxx-xxxx'
        },
        "transaction": {
            "fired": "2018-12-27T11:41:40.249Z",
            "$comment": "My comment from the call form"
        }
    }
    call_id, result = process(session, input_data)
    assert not call_id

def test_invalid_input2(session, state):

    input_data = {
        "contact": {},
        "transaction": {
            "fired": "2018-12-27T11:41:40.249Z",
            "comment": "My comment from the call form"
        }
    }
    call_id, result = process(session, input_data)
    assert not call_id

def test_assert_input__eq__output(session, state):

    input_data = {
        "contact": {
            "$ref": CONTACT_ID
        },
        "transaction": {
            "fired": "2018-12-27T11:41:40.249Z",
            "$comment": "My comment from the call form"
        }
    }
    call_id, result = process(session, input_data)

    assert call_id
    assert result

    contact = session.get_entry(Contact.module, CONTACT_ID)
    call = session.get_entry(Call.module, call_id)

    for field in FIELDS:
        found = list(
            filter(lambda options: options.get('name') == field, result))

        assert found
        assert len(found) == 1
        assert found[0].get('value') == getattr(call, field)