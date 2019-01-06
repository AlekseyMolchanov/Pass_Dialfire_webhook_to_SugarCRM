#!/usr/bin/env python
# encoding: utf-8

import os
import pytest
from sugarcrm import Call, Task
from connection import connect
from processor import process

from const import FIELDS

TASK_ID = "56decc66-6ab7-e544-71ac-5c326c701c0e"


@pytest.fixture(scope="module")
def session(request):
    session = connect()
    return session


@pytest.fixture(scope="module")
def state(request):
    __state = {'account': None}
    return __state


def test_env(session, state):
    assert os.environ.get('SERVER_HOST')
    assert os.environ.get('SERVER_PORT')
    assert os.environ.get('SUGAR_CRM_URL')

    assert os.environ.get('SUGAR_CRM_USERNAME')
    assert os.environ.get('SUGAR_CRM_PASSWORD')
    assert os.environ.get('SUGAR_CRM_ASSIGNED_USER_ID')


def test_source_task(session, state):
    task = session.get_entry(Task.module, TASK_ID)
    assert task


def test_assert_input__eq__output(session, state):

    input_data = {
        "contact": {
            "$ref": TASK_ID,
            "transaction": {
                "comment": "My comment from the call form"
            },
            "fired": "2018-12-27T11:41:40.249Z",
        }
    }
    call_id, result = process(session, input_data)

    assert call_id
    assert result

    task = session.get_entry(Task.module, TASK_ID)
    call = session.get_entry(Call.module, call_id)

    for field in FIELDS:
        found = list(
            filter(lambda options: options.get('name') == field, result))

        assert found
        assert len(found) == 1
        assert found[0].get('value') == getattr(call, field)