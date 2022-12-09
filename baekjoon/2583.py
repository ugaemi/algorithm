import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n, k = map(int, sys.stdin.readline().strip().split())
graph = [[0 for _ in range(m)] for _ in range(n)]

dots = []
for _ in range(k):
    dot = list(map(int, sys.stdin.readline().strip().split()))
    dots.append([dot[:2], dot[2:]])

for i in range(k):
    for a in range(dots[i][0][0], dots[i][1][0]):
        for b in range(dots[i][0][1], dots[i][1][1]):
            graph[a][b] = 1


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    area = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                area += 1
    return area


areas = []
for a in range(n):
    for b in range(m):
        if graph[a][b] == 0:
            areas.append(bfs(graph, a, b))

print(len(areas))
print(" ".join(map(str, sorted(areas))))
