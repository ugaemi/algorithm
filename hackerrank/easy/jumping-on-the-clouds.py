import os


def jumpingOnClouds(c):
    jump, now = 0, 0
    while len(c) - 1 > now + 2:
        if c[now + 2] == 0:
            now += 2
        else:
            now += 1
        jump += 1
    return jump + 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + "\n")

    fptr.close()
