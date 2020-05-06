#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = float(meal_cost*(tip_percent/100))
    tax = float(meal_cost*(tax_percent/100))
    total_cost = float(meal_cost+tip+tax)
    if total_cost - int(total_cost) > 0.5:
        print(int(total_cost+1))
    else:
        print(int(total_cost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
