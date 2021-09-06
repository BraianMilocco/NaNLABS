import os 
import requests
import json
from .apiGeneral import url, headers, valid_categories

def create_issue(json_):

    query = {
    'idList': os.getenv('trelloToDo', None),
    'name': json_.get('title'),
    'desc ': json_.get('description')
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    return  {'issue':'created'}