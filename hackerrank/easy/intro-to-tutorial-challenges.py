def introTutorial(V, arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == V:
            return mid
        elif arr[mid] < V:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # If the value is not found in the array
