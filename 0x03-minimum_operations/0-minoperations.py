#!/usr/bin/python3
"""
Method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    if n <= 1:
        return 0
    nOperations = 2

    hsInFile = 2
    clipboardHs = 1

    while hsInFile < n:
        if n % hsInFile == 0:
            clipboardHs = hsInFile
            nOperations += 1
        hsInFile += clipboardHs
        nOperations += 1
    return nOperations
