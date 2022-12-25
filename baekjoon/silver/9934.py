import sys

k = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
result = [[] for _ in range(k)]


def print_node(i, start, end):
    mid = start + (end - start) // 2
    result[i].append(nodes[mid])
    if end - start > 2:
        print_node(i + 1, start, mid - 1)
        print_node(i + 1, mid + 1, end)
    else:
        result[i + 1].append(nodes[start])
        result[i + 1].append(nodes[end])


print_node(0, 0, len(nodes) - 1)
for nodes in result:
    print(" ".join(map(str, nodes)))
