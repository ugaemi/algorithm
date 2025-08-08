import math
import os
import random
import re
import sys
from collections import Counter


def sherlockAndAnagrams(s):
    n = len(s)
    counter = Counter()

    for i in range(n):
        freq = [0] * 26
        for j in range(i, n):
            char_index = ord(s[j]) - ord('a')
            freq[char_index] += 1
            counter[tuple(freq)] += 1
            print(f"i={i}, j={j}, char={s[j]}, freq={freq}, counter={counter[tuple(freq)]}")

    result = 0
    for key, count in counter.items():
        if count > 1:
            result += count * (count - 1) // 2  # nC2
            print(f"key={key}, count={count}, 쌍={count*(count-1)//2}")

    return result


if __name__ == '__main__':
    sherlockAndAnagrams(input())
