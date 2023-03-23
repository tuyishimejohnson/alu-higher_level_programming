#!/usr/bin/python3

import sys
import signal

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {c: 0 for c in status_codes}
total_size = 0
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        count = status_counts[code]
        if count > 0:
            print(f"{code}: {count}")

def handle_sigint(signum, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

for line in sys.stdin:
    try:
        _, _, _, status, size = line.strip().split()
        status = int(status)
        size = int(size)
    except ValueError:
        continue
    if status in status_counts:
        status_counts[status] += 1
    total_size += size
    line_count += 1
    if line_count % 10 == 0:
        print_stats()
