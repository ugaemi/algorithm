import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())
count = 0


def dfs(k):
    tree[k] = -2
    for i in range(n):
        if k == tree[i]:
            dfs(i)


dfs(remove_node)

for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        count += 1

print(count)
