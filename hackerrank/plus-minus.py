#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    list_size = len(arr)
    positive_counter = 0
    zero_counter = 0
    negative_counter = 0
    for number in arr:
        if(number > 0):
            positive_counter = positive_counter + 1
        elif(number == 0):
            zero_counter = zero_counter + 1
        elif(number < 0):
            negative_counter = negative_counter + 1
    print("{0:.6f}".format(positive_counter / list_size))
    print("{0:.6f}".format(negative_counter / list_size))
    print("{0:.6f}".format(zero_counter / list_size))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
