import os 
import requests
import json
import random
from .apiGeneral import url, headers

def create_bug(json_):

    member = get_member()

    query = {
    'idList': os.getenv('trelloToDo', None),
    'name': 'BUG',
    'desc': json_.get('description'),
    'idMembers':   [ member ]
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    print(response.text)
    return  {'bug':'created'}

def get_member():

    url_members = "https://api.trello.com/1/boards/{}/members?key={}&token={}".format(
        os.getenv('trelloBoard', None),
        os.getenv('trelloKey', None), 
        os.getenv('trelloToken', None)
    )

    response = requests.request("GET",url_members)

    members = response.json()
    members_cant = len(response.json()) - 1
    id_random =  random.randint(0,members_cant)

    return members[id_random]['id']