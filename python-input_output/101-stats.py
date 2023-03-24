#!/usr/bin/env python3

import sys

# Initialize variables
file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0

# Define a function to print metrics
def print_metrics():
    print(f"File size: {file_size}")
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")
    print()

# Read stdin line by line and compute metrics
try:
    for line in sys.stdin:
        line_count += 1
        ip, _, _, status_code, size = line.split()
        file_size += int(size)
        status_codes[int(status_code)] += 1
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()

