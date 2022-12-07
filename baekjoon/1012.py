import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(sys.stdin.readline().strip())


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


for _ in range(t):
    answer = 0
    m, n, k = map(int, sys.stdin.readline().strip().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[x][y] = 1
    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1:
                bfs(graph, x, y)
                answer += 1
    print(answer)
