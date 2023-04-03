#!/usr/bin/env python3
""" Importing the request from the taken URL and with the email as a parameter"""


import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
