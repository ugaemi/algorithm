# 한국이 그리울 땐 서버에 접속하지
import sys

n = int(sys.stdin.readline())
pattern = sys.stdin.readline().rstrip()
p = pattern.split("*")

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if len("".join(p)) > len(s) and s[: len(p[0])] == p[0] and s[-len(p[1]) :] == p[1]:
        print("DA")
    else:
        print("NE")
