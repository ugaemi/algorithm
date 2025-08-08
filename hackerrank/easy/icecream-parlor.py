def icecreamParlor(m, arr):
    seen = {}
    for i, price in enumerate(arr):
        complement = m - price
        if complement in seen:
            return [seen[complement] + 1, i + 1]
        seen[price] = i
    return []


if __name__ == '__main__':
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])  # Number of test cases
    index = 1
    results = []

    for _ in range(t):
        m = int(data[index])  # Total money available
        n = int(data[index + 1])  # Number of ice cream flavors
        arr = list(map(int, data[index + 2].split()))  # Prices of the ice cream flavors
        result = icecreamParlor(m, arr)
        results.append(" ".join(map(str, result)))
        index += 3

    print("\n".join(results))
