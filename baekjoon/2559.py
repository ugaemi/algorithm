# 수열
import sys

n, k = map(int, sys.stdin.readline().split())
temperatures = list(map(int, sys.stdin.readline().split()))

result = [sum(temperatures[:k])]

for i in range(n - k):
    result.append(result[i] - temperatures[i] + temperatures[k + i])

print(max(result))
