#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as error:
        raise ValueError("Matrices cannot be multiplied.") from error
