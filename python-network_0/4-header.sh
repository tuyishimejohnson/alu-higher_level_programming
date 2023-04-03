#!/bin/bash
# Script that takes a URL as an argument, send get requet and displays the body
curl -sH "X-School-User-Id: 98" "$1"
