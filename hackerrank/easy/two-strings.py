def twoStrings(s1, s2):
    # Convert both strings to sets to find common characters
    set1 = set(s1)
    set2 = set(s2)

    # Check if there is any intersection between the two sets
    if set1.intersection(set2):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])  # Number of test cases
    results = []

    for i in range(1, 2 * t, 2):
        s1 = data[i]
        s2 = data[i + 1]
        result = twoStrings(s1, s2)
        results.append(result)

    print("\n".join(results))
