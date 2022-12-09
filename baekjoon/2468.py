import sys
from collections import deque
from copy import deepcopy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

size = int(sys.stdin.readline().strip())

graph = []
min_h, max_h = 100, 2
for x in range(size):
    heights = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(heights)
    min_h, max_h = min(min_h, min(heights)), max(max_h, max(heights))


def bfs(temp_graph, x, y, h):
    queue = deque()
    queue.append((x, y))
    temp_graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if temp_graph[nx][ny] > h:
                temp_graph[nx][ny] = 0
                queue.append((nx, ny))


result = []
for h in range(min_h - 1, max_h):
    temp_graph = deepcopy(graph)
    temp_answer = 0
    for x in range(size):
        for y in range(size):
            if temp_graph[x][y] > h:
                bfs(temp_graph, x, y, h)
                temp_answer += 1
    result.append((h, temp_answer))

print(max(result, key=lambda x: x[1])[1])
