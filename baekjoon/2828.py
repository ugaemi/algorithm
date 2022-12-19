import sys

n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline().strip())
apples = [int(sys.stdin.readline()) for _ in range(j)]

answer, s = 0, 1
for apple in apples:
    while True:
        if apple in [*range(s, s + m)]:
            break
        else:
            if apple < s:
                s -= 1
            else:
                s += 1
            answer += 1

print(answer)
