import os

try:
    assigned_user_id = os.environ['SUGAR_CRM_ASSIGNED_USER_ID']
    server_host = os.environ['SERVER_HOST']
    server_port = os.environ['SERVER_PORT']
    server_debug = bool(int(os.environ['SERVER_DEBUG']))
except:
    print('''
######## Warning ########
You must define Environment Variables:
SERVER_HOST, SERVER_PORT, SERVER_DEBUG
and SUGAR_CRM_ASSIGNED_USER_ID
###########################\n''')
    exit(1)

FMT_IN = "%Y-%m-%dT%H:%M:%S.%fZ"
FMT_OUT = "%Y-%m-%d %H:%M:%S"

FIELDS = [
    'description', 'deleted', 'date_start', 'parent_type', 'parent_name',
    'status', 'direction', 'parent_id', 'assigned_user_id', 'name'
]
