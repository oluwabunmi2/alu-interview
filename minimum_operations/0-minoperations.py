#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """
    given a number n, calculate the fewest no. of operations
    that result to n and H characters in the file.
    """

    if n <= 1:
        return 0

    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n/i)) + i
    return n
