#!/bin/bash
# This program takes in a URL, sends a request to that URL, and displays the size of the body of the response.
if [ $# -ne 1 ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

response=$(curl -s -w "%{size_download}" -o /dev/null "$1")

echo "Size of the body of the response: $response bytes"

