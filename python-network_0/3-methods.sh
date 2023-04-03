#!/bin/bash
# A script that takes in the URL and displays all http
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
