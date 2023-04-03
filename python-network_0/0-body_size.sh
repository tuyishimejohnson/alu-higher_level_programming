#!/bin/bash
# A script that takes in URL sends a request and displays the size of the body.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
