#!/usr/bin/python3
"""
12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    function to print pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        ro = [1]
        for j in range(1, i):
            ro.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        ro.append(1)
        triangle.append(ro)
    return triangle
