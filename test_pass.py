#!/usr/bin/env python
# encoding: utf-8

import os
import pytest
from sugarcrm import Call, Task
from connection import connect
from processor import process

from const import FIELDS


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


def test_assert_input__eq__output(session, state):

    task_id = "56decc66-6ab7-e544-71ac-5c326c701c0e"

    input_data = {
        "contact": {
            "$ref": task_id,
            "transaction": {
                "comment": "My comment from the call form"
            },
            "fired": "2018-12-27T11:41:40.249Z",
        }
    }
    call_id, result = process(session, input_data)

    assert call_id
    assert result

    task = session.get_entry(Task.module, task_id)
    call = session.get_entry(Call.module, call_id)

    for field in FIELDS:
        found = list(
            filter(lambda options: options.get('name') == field, result))

        assert found
        assert len(found) == 1
        assert found[0].get('value') == getattr(call, field)