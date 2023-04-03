#!/usr/bin/env python3
""" Importing requests and sys"""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    response = requests.post(url, data=payload)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
