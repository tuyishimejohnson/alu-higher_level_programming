#!/usr/bin/python3
"""Importing a URL"""


import urllib.request
import sys

'''Get the URL from the command line arguments'''
url = sys.argv[1]

'''Send a request to the URL'''
req = urllib.request.Request(url)

'''Open the URL and read the response headers'''
with urllib.request.urlopen(req) as response:
    headers = response.info()

 '''Extract the value of the X-Request-Id variable from the headers'''
x_request_id = headers.get('X-Request-Id')

# Display the value of the X-Request-Id variable
print(x_request_id)

