import os 
import requests
import json
from .apiGeneral import url, headers
from .messages import error_message
from .apiGeneral import  url, headers, valid_categories

def create_task(json_):

    if json_.get('category') not in valid_categories:
        return error_message
        
    idLabel = str(os.getenv(json_.get('category'), None))
    query = {
    'idList': os.getenv('trelloToDo', None),
    'idLabels': [idLabel],
    'name': json_.get('title')
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    return  {'task':'created'}#json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
