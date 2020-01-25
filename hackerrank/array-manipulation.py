def arrayManipulation(n, queries):
    result = [0] * (n + 1)
    max_value = -1
    for query in queries:
        start = query[0] - 1
        end = query[1]
        result[start] += query[2]
        result[end] += -query[2]
    tmp = 0
    for r in result:
        tmp += r
        if max_value < tmp:
            max_value = tmp
    return max_value


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(str(result))
