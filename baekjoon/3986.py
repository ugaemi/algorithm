import sys

number = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(number)]

answer = 0
for word in words:
    stack = []
    for s in word:
        if len(stack) and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if len(stack) == 0:
        answer += 1

print(answer)
