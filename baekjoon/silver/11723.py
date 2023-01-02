import sys

M = int(input())
S = set()
for _ in range(M):
    splitted = sys.stdin.readline().split()
    if len(splitted) == 1:
        op = splitted[0]
        if op == "all":
            S = set(i for i in range(1, 21))
        elif op == "empty":
            S = set()
    else:
        op, n = splitted
        n = int(n)
        if op == "add":
            S.add(n)
        elif op == "remove":
            S.discard(n)
        elif op == "check":
            if n in S:
                print(1)
            else:
                print(0)
        elif op == "toggle":
            if n in S:
                S.remove(n)
            else:
                S.add(n)
