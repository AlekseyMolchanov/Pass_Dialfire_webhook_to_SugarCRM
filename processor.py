#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

'''
Input[2] | Necessary fields only
───────────────
┌────
│ {
│   "contact": {
│       "$ref": "3D9d92b1f4-c13c-e7d8-0931-5c0feae1f7c3",
│       "transaction": {
│           "comment": "My comment from the call form"
│       }
│       "fired": "2018-12-27T11:41:40.249Z",
│   }
│ }
└────

Expected output
───────────────
┌────
│ [
│   {'name': 'module', 'value': 'Calls'},
│   {'name': 'description','value': 'My comment from the call form',
│   {'name': 'deleted', 'value': '0'},
│   {'name': 'date_start', 'value': '2018-12-27T11:41:40.249Z'},
│   {'name': 'parent_type', 'value': 'crm.$ref'},
│   {'name': 'parent_name', 'value': 'crm.$ref.name'},
│   {'name': 'status', 'value': 'Held'},
│   {'name': 'direction', 'value': 'Outbound'},
│   {'name': 'parent_id', 'value': '$ref'},
│   {'name': 'assigned_user_id', 'value': '1491fcc2-c6f3-11e8-9407-0ea10e74340a'},
'''

from sugarcrm import Call, Task
from const import FMT_IN, FMT_OUT, assigned_user_id, FIELDS

def process(session, input_data):

    contact = input_data.get('contact') or {}
    task_id = contact.get('$ref')
    fired = contact.get('fired')
    description = contact.get('transaction', {}).get('comment')
    if not task_id:
        return dict(result=False, message="task_id not set")
    
    task = session.get_entry(Task.module, task_id)
    if not task:
        return dict(result=False, message="Task not found [%s]" % task_id)

    dt_fired = datetime.strptime(fired, FMT_IN)

    obj = Call()
    obj.status = 'Held'
    obj.direction = 'Outbound'
    obj.name = 'Outbound call with dialfire'
    obj.deleted = '0'
    obj.description = description
    obj.date_start = dt_fired.strftime(FMT_OUT)
    obj.parent_type = Task.module
    obj.parent_id = task.id
    obj.parent_name = task.name
    obj.assigned_user_id = assigned_user_id

    call = session.set_entry(obj)

    result = [{'name': 'module', 'value': 'Calls'}]
    for field in FIELDS:
        result.append(dict(name=field, value=getattr(call, field, None)))
    
    return call.id, result 
    
