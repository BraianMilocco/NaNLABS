def post_type(json_):
    type_ = json_.get('type')
    return type_.lower() if type_ else None

def validate_bug(json_):
    return True if json_.get('description') else False

def validate_issue(json_):
    title = json_.get('title')
    description = json_.get('description')

    return True if (title and description) else False

def validate_task(json_):
    categories = ['Maintenance', 'Research', 'Test']
    category = json_.get('category')
    if category not in categories:
        return False
    return True if json_.get('title') else False

validator = {
    'bug': validate_bug,
    'issue': validate_issue,
    'task': validate_task
}