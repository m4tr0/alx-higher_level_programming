#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed at the current position (row, col)
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def place_queens(board, row, N):
    # Base case: all queens have been placed
    if row == N:
        print_solution(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen

            # Recursively place queens in the next row
            place_queens(board, row + 1, N)

            board[row][col] = 0  # Remove the queen (backtrack)

def print_solution(board, N):
    # Print the positions of queens in the current solution
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

if __name__ == "__main__":
    # Validate the input
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

    # Create an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N Queens problem
    place_queens(board, 0, N)
