package programmers

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func InsufficientAmount(price, money, count int) int {
    requiredAmount := 0
    for i := 1; i < count + 1; i++ {
    	requiredAmount += i * price
    }
    return Abs(min(money - requiredAmount, 0))
}
