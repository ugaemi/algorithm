import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

h, w = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
cheeses = []


def bfs():
    count = 0
    visited[0][0] = 1
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                else:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    count += 1
    cheeses.append(count)
    return count


time = 0
while True:
    time += 1
    visited = [[0] * w for _ in range(h)]
    if bfs() == 0:
        break

print(time - 1)
print(cheeses[-2])
