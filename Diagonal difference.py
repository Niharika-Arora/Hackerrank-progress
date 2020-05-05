#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    prim = 0
    secd = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                prim = prim + arr[i][j]
            if i == len(arr) - j - 1:
                secd = secd + arr[i][j]
    diff = abs(prim - secd)
    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
