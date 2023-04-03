#!/bin/bash
# Script that takes in a URL sends GET request and diplays only body of a 200  status
curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
