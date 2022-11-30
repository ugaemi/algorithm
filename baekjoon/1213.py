import sys

from collections import defaultdict


s = sys.stdin.readline().strip()
d = defaultdict(int)

for c in s:
    d[c] += 1

center = ""
for c in d:
    if d[c] % 2 != 0:
        if center:
            print("I'm Sorry Hansoo")
            break
        center = c
else:
    answer = ""
    for c, count in sorted(d.items()):
        answer += c * (count // 2)
    print(answer + center + answer[::-1])
