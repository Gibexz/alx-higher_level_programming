#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.

"""
def matrix_divided(matrix, div):
    """
    function that divides the elements (ints or floats) of a matrix

    Args:
    matrix: list of a lists of integers/floats
    div: divisor

    Returns:
    A new matrix

    Raises:
        TypeError:
        if the matrix is not a list of list
        if the content of the matrix is not floats/integers
        if the rows sof the matrix are not of the same size
        if div is not an int/float

        ZeroDivisionError:
        if div is equal to 0.

    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg1)

    len_m = 0

    for rows in matrix:
        if not rows or not isinstance(rows, list):
            raise TypeError(msg1)

        if len_m != 0 and len(rows) != len_m:
            raise TypeError(msg2)

        for num in rows:
            if type(num) not in [int, float]:
                raise TypeError(msg1)

        len_m = len(rows)

    result = []
    for row in matrix:
        result.append([round(x/div, 2) for x in row])

    return result
