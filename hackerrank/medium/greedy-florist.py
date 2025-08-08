def getMinimumCost(k, c):
    c.sort(reverse=True)

    total_cost = 0
    for i in range(len(c)):
        purchase_count = (i // k) + 1
        total_cost += c[i] * purchase_count

    return total_cost
