#!/bin/bash
# Script that takes in a URL sends a post request to the passed URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
