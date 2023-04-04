#!/usr/bin/python3
""" Github API by importing requests"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

response = requests.get("https://api.github.com/user", auth=(username, password))

if response.status_code == 200:
    data = response.json()
    print(data['id'])
else:
    print(None)



