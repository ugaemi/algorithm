import sys
from collections import deque

subin, sister = map(int, sys.stdin.readline().split())
road = [-1] * 100001
result = 0

queue = deque()
queue.append(subin)
road[subin] = 0

while queue:
    now = queue.popleft()
    if now == sister:
        result += 1
        continue
    for i in (now - 1, now + 1, 2 * now):
        if 0 <= i <= 100000 and (road[i] == road[now] + 1 or road[i] == -1):
            road[i] = road[now] + 1
            queue.append(i)

print(road[sister])
print(result)
