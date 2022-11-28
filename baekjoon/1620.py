import sys

from collections import defaultdict

nums, questions = map(int, sys.stdin.readline().split())
encyclopedia = defaultdict(int)

for i in range(nums):
    poketmon = sys.stdin.readline().strip()
    encyclopedia[poketmon] = i + 1
    encyclopedia[str(i + 1)] = poketmon

for i in range(questions):
    print(encyclopedia[sys.stdin.readline().strip()])
