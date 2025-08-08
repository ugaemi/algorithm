def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        min_diff = min(min_diff, diff)

    return min_diff


if __name__ == '__main__':
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])  # Number of elements in the array
    arr = list(map(int, data[1].split()))  # The array elements

    result = minimumAbsoluteDifference(arr)
    print(result)
