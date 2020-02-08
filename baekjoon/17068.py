import sys

num_of_block = int(sys.stdin.readline())
blocks = []
result = 1

for i in range(num_of_block):
    blocks.append(int(sys.stdin.readline()))

tmp = blocks[-1]
for i in range(num_of_block-2, -1, -1):
    if blocks[i] > tmp:
        result += 1
        tmp = blocks[i]

print(result)
