#!/bin/bash
# Script that takes a URL as an argument, send get requet and displays the body
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
