#!/usr/bin/python3
""" Github API by importing requests"""


import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = tuyishimejohnson
    token = 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

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        response_json = response.json()
        print(response_json["id"])
    else:
        print("Error: {}".format(response.status_code))

