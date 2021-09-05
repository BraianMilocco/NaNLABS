import os 
import requests
import json

def create_task(json_):
    url = "https://api.trello.com/1/cards?key={}&token={}".format(os.getenv('trelloKey', None), os.getenv('trelloToken', None))
    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': os.getenv('trelloToDo', None),
    'idLabels': [str(os.getenv(json_.get('category'), None))],
    'name': json_.get('title')
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
