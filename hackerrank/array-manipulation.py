def arrayManipulation(n, queries):
    last_array = [0] * n
    for query in queries:
        start = query[0] - 1
        end = query[1]
        for i in range(start, end):
            last_array[start] += query[2]
            start += 1
    return max(last_array)


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(str(result))
