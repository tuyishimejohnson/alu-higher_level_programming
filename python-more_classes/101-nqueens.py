#!/usr/bin/python3
import sys

# Define a function to check if a given placement of queens is valid


def is_valid(queens):
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if two queens are on the same row or diagonal
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                return False
    return True


# Define a recursive function to find all valid placements of queens
def find_solutions(queens, n):
    if len(queens) == n:
        # If a valid placement of queens has been found, print it
        if is_valid(queens):
            print(" ".join(str(q) for q in queens))
    else:
        # Try adding a queen to each column in the next row
        for i in range(n):
            if i not in queens:
                find_solutions(queens + [i], n)

# Check the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Find all valid placements of queens on an NxN board
find_solutions([], n)
