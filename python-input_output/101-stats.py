#!/usr/bin/env python3

import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

for i, line in enumerate(sys.stdin):
    try:
        ip, _, _, _, status_code, size = line.split()
        status_code = int(status_code)
        size = int(size)

        total_size += size
        status_counts[status_code] += 1

        if i > 0 and i % 10 == 0:
            print_stats()

    except ValueError:
        pass

print_stats()

