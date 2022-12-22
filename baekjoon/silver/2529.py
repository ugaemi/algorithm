import sys
from itertools import permutations

n = int(sys.stdin.readline())
inequalities = sys.stdin.readline().split()

results = []
for p in permutations(range(0, 10), n + 1):
    correct = True
    for i, inequality in enumerate(inequalities):
        if (inequality == "<" and p[i] > p[i + 1]) or (inequality == ">" and p[i] < p[i + 1]):
            correct = False
            break
    if correct:
        results.append("".join(map(str, p)))


print(max(results))
print(min(results))
