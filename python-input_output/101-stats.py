#!/usr/bin/python3
"""Importing sys"""

import sys

"""Initialize variables to hold metrics"""
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    """Loop through standard input"""
    for line in sys.stdin:
        # Increment line count
        line_count += 1
        
        # Split input line by spaces
        parts = line.split()

        # Extract file size and status code
        size = int(parts[-1])
        status = int(parts[-2])

        # Add file size to total
        total_size += size

        # Increment status count
        if status in status_counts:
            status_counts[status] += 1

        """If 10 lines have been processed, print statistics"""
        if line_count == 10:
            print(f"Total file size: {total_size}")
            for status, count in sorted(status_counts.items()):
                if count > 0:
                    print(f"{status}: {count}")
            print()
            line_count = 0

except KeyboardInterrupt:
    # Print final statistics on keyboard interrupt
    print(f"Total file size: {total_size}")
    for status, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status}: {count}")

