import copy
import sys
from collections import deque
from itertools import combinations

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]
empty = [(i, j) for j in range(m) for i in range(n) if graph[i][j] == 0]
virus_queue = deque((i, j) for j in range(m) for i in range(n) if graph[i][j] == 2)
safety_zone = 0

for w_c in combinations(empty, 3):
    tmp_graph = copy.deepcopy(graph)
    for i, j in w_c:
        tmp_graph[i][j] = 1
    queue = copy.deepcopy(virus_queue)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))
    cnt = 0
    for row in tmp_graph:
        cnt += row.count(0)
    safety_zone = max(safety_zone, cnt)

print(safety_zone)
