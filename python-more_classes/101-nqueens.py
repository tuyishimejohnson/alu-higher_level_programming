#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if it's safe to place a queen in (row, col)
    # along the current board state
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    for i in range(N):
        for j in range(N):
            if (i+j == row+col) or (i-j == row-col):
                if board[i][j] == 1:
                    return False
    return True

def solve_n_queens(board, col, N):
    # Recursive function to solve the N Queens problem
    if col == N:
        # Base case: all queens are placed on the board
        # Print the solution
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=" ")
            print()
        print()
        return True
    found_solution = False
    for row in range(N):
        if is_safe(board, row, col, N):
            # Place a queen in (row, col)
            board[row][col] = 1
            # Recursive call to solve for the next column
            if solve_n_queens(board, col+1, N):
                found_solution = True
            # Backtrack: remove the queen from (row, col)
            board[row][col] = 0
    return found_solution

# Main program
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for x in range(N)] for y in range(N)]

solve_n_queens(board, 0, N)


