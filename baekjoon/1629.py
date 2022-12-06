import sys

a, b, c = map(int, sys.stdin.readline().strip().split())


def divide_and_conquer(x, y, z):
    if y == 1:
        return x % z
    temp = divide_and_conquer(x, y // 2, z)
    if y % 2 == 0:
        return temp * temp % z
    else:
        return temp * temp * a % z


print(divide_and_conquer(a, b, c))
