#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    hh = s[0:2]
    period = s[-2:]
    if period == "AM":
        if hh == '12':
            output = '00'+s[2:-2]
        else:
            output = s[0:-2]
    if period == "PM":
        if hh == '12':
            output = s[0:-2]
        else:
            output = str(int(hh)+12) + s[2:-2]
    return output


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
