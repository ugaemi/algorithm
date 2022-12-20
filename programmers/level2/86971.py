import unittest
from collections import deque


def bfs(node, visited, tree):
    queue = deque([node])
    cnt = 1
    visited[node] = True
    while queue:
        now = queue.popleft()
        for i in tree[now]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True
    return cnt


def power_grid(n, wires):
    answer = n
    tree = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
    for node1, node2 in wires:
        visited = [False] * (n + 1)
        visited[node2] = True
        result = bfs(node1, visited, tree)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))
    return answer


class PowerGridTest(unittest.TestCase):
    def test_power_grid(self):
        self.assertEqual(power_grid(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]), 3)
        self.assertEqual(power_grid(4, [[1, 2], [2, 3], [3, 4]]), 0)
        self.assertEqual(power_grid(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]), 1)
