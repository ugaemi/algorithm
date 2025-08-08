def luckBalance(k, contests):
    result = 0

    important_contest_lucks = []
    for contest in contests:
        if contest[1] == 1:
            important_contest_lucks.append(contest[0])
        else:
            result += contest[0]

    important_contest_lucks.sort(reverse=True)
    result += sum(important_contest_lucks[:k]) - sum(important_contest_lucks[k:])
    return result


if __name__ == '__main__':
    n, k = map(int, input().split())
    contests = [list(map(int, input().split())) for _ in range(n)]

    result = luckBalance(k, contests)
    print(result)
