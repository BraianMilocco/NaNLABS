import os 

url = "https://api.trello.com/1/cards?key={}&token={}".format(os.getenv('trelloKey', None), os.getenv('trelloToken', None))

headers = {"Accept": "application/json"}

valid_categories= ['Maintenance','Test','Research']


from .issue import create_issue
from .task import create_task
from .bug  import create_bug

functions_card= {
"bug": create_bug,
"task": create_task,
"issue": create_issue
}