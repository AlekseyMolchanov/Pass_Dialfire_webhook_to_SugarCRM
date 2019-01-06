import os

ASSIGNED_USER_ID = os.environ.get('SUGAR_CRM_ASSIGNED_USER_ID')

FMT_IN = "%Y-%m-%dT%H:%M:%S.%fZ"
FMT_OUT = "%Y-%m-%d %H:%M:%S"

FIELDS = [
    'description', 'deleted', 'date_start', 'parent_type', 'parent_name',
    'status', 'direction', 'parent_id', 'assigned_user_id', 'name'
]
