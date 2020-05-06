#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.


def birthdayCakeCandles(ar,ar_count):
    maxm = ar[0]
    count = 0
    for i in range(1, ar_count):
        if maxm < ar[i]:
            maxm = ar[i]
    for j in range(ar_count):
        if ar[j] == maxm:
            count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar,ar_count)

    fptr.write(str(result) + '\n')

    fptr.close()
