from collections import defaultdict


def countTriplets(arr, r):
    left = defaultdict(int)
    right = defaultdict(int)

    for num in arr:
        right[num] += 1

    count = 0
    for x in arr:
        print(f"Processing {x}: left={dict(left)}, right={dict(right)}, count={count}")
        right[x] -= 1
        if x % r == 0:
            left_count = left[x // r]
            right_count = right[x * r]
            count += left_count * right_count
        left[x] += 1

    return count


if __name__ == '__main__':
    n, r = map(int, input().split())
    arr = list(map(int, input().split()))
    result = countTriplets(arr, r)
    print(result)
