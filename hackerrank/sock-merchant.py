#!/bin/python3

import os
from collections import defaultdict


def sockMerchant(n, ar):
    d = defaultdict(int)
    answer = 0
    while ar:
        n = ar.pop()
        if d[n] == 0:
            d[n] += 1
        else:
            answer += 1
            d[n] = 0
    return answer


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
