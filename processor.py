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

from sugarcrm import Call, Contact, User
from const import FMT_IN, FMT_OUT, ASSIGNED_USER_ID, FIELDS
from logging import getLogger

logger = getLogger('process')

def process(session, input_data):

    contact = input_data.get('contact')
    contact_id = contact.get('$ref')
    logger.debug('contact_id: {}'.format(contact_id))
    
    transaction = input_data.get('transaction')
    fired = transaction.get('fired')
    logger.debug('fired: {}'.format(fired))
    
    description = contact.get('$comment')
    logger.debug('description: {}'.format(description))

    if not contact_id:
        return None, []
    
    contact = session.get_entry(Contact.module, contact_id)
    logger.debug('contact: {}'.format(contact))

    logger.debug('assigned_user_id: {}'.format(ASSIGNED_USER_ID))
    user = session.get_entry(User.module, ASSIGNED_USER_ID)
    logger.debug('User: {}'.format(user))

    if not contact:
        return None, []

    dt_fired = datetime.strptime(fired, FMT_IN)

    obj = Call()
    obj.status = 'Held'
    obj.direction = 'Outbound'
    obj.name = 'Outbound call with dialfire'
    obj.deleted = '0'
    obj.description = description
    obj.date_start = dt_fired.strftime(FMT_OUT)
    obj.parent_type = Contact.module
    obj.parent_id = contact.id
    obj.parent_name =  "{} {}".format(contact.first_name, contact.last_name).strip()
    obj.assigned_user_id = ASSIGNED_USER_ID

    call = session.set_entry(obj)
    logger.debug('call: {}'.format(call))
    logger.debug('call id: {}'.format(call.id))

    result = [{'name': 'module', 'value': 'Calls'}]
    for field in FIELDS:
        result.append(dict(name=field, value=getattr(call, field, None)))
    
    return call.id, result 
    
