#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can execute only two operations in this file
    """

    if n <= 1:
        return 0

    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n/i)) + i
    return n
