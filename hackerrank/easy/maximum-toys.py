def maximumToys(prices, k):
    # Sort the prices in ascending order
    prices.sort()

    # Initialize the number of toys and total cost
    num_toys = 0
    total_cost = 0

    # Iterate through the sorted prices
    for price in prices:
        if total_cost + price <= k:
            total_cost += price
            num_toys += 1
        else:
            break  # Stop if we can't afford the next toy

    return num_toys


if __name__ == "__main__":
    # Example usage
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    result = maximumToys(prices, k)
    print(result)
