import datetime
import json
import requests # A dependency.

def hello():
    print(json.dumps(stats()))

def stats(message='Hello Packaging', url='https://pyconbalkan.com'):
    """
    Returns a dict with date, statuscode and page size.
    """
    r = requests.get(url)
    return {
        'message': message,
        'time': datetime.datetime.today(),
        'status_code': r.status_code,
        'size': len(r.content),
    }

