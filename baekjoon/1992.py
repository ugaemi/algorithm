import sys


n = int(sys.stdin.readline().strip())
data = [list(input()) for _ in range(n)]
answer = ""


def compression(r, c, size):
    if size == 1:
        print(data[r][c], end="")
        return

    num = data[r][c]
    for i in range(r, r + size):
        for j in range(c, c + size):
            if num != data[i][j]:
                print("(", end="")
                size //= 2
                compression(r, c, size)
                compression(r, c + size, size)
                compression(r + size, c, size)
                compression(r + size, c + size, size)
                print(")", end="")
                return

    print(data[r][c], end="")
    return


compression(0, 0, n)
