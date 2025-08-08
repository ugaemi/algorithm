def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        left_to_right += arr[i][i]
        right_to_left += arr[i][len(arr)-1-i]
    return abs(left_to_right - right_to_left)


if __name__ == '__main__':
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])  # Size of the square matrix
    arr = [list(map(int, data[i + 1].split())) for i in range(n)]  # The square matrix

    result = diagonalDifference(arr)
    print(result)
