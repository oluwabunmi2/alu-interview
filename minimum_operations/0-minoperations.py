#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """

    if not n or n < 2:
        return 0
    numberOperations = 0
    for time in range(2, n+1):
        while(n % time == 0):
            numberOperations += time
            n = n / time
    return(numberOperations)
