#!/usr/bin/python3
"""
This module provides a function for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and returns a new matrix.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by the given number.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix doesn't have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    num_rows = len(matrix)
    if num_rows == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    num_cols = len(matrix[0])
    if num_cols == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != num_cols:
            raise TypeError("Each row of the matrix must have the same size")

        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
