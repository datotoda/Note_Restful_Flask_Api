from time import sleep
from urllib import response
import requests

BASE = 'http://127.0.0.1:5000/'

notes = {
    1: {
        "title": "first",
        "body": "note"
    },
    2: {
        "title": "second",
        "body": "Flask Restful Api"
    },
    3: {
        "title": "account",
        "body": "email: admin@gmail.com\npass: admin"
    }
}


for k, v in notes.items():
    response = requests.post(BASE + 'note/%d' % k, data=v)
    print(response.json())
    input()

for k in notes:
    response = requests.delete(BASE + 'note/%d' % k)
    print(response.json())
