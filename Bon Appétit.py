#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    s = 0
    n = len(bill)
    for i in range(0,n):
        if i == k:
            continue
        else:
            s += bill[i]
    b_act = s//2
    if b_act == b:
        print("Bon Appetit")
    else:
        print(b - b_act)


if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
