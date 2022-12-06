import sys

number = int(sys.stdin.readline().strip())
target_number = int(sys.stdin.readline().strip())
armors = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
num_set = set()
for armor in armors:
    if target_number - armor in num_set:
        answer += 1
    else:
        num_set.add(armor)

print(answer)
