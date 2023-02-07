#!/usr/bin/python3
"""minimum Operations"""


def minOperations(n):
    """Returns an integer
    If n is impossible to achieve, return 0"""

     if n <= 1:
        return 0

    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n/i)) + i
    return n

