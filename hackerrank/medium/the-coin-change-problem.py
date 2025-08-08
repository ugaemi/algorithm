def getWays(n, coins):
    ways = [0] * (n + 1)
    ways[0] = 1  # There's one way to make change for 0

    for coin in coins:
        for amount in range(coin, n + 1):
            ways[amount] += ways[amount - coin]

    return ways[n]
