function insufficientAmount(price, money, count) {
  let requiredAmount = 0;
  for (let i=1; i<count+1; i++) {
    requiredAmount += i * price;
  }
  return Math.abs(Math.min(money - requiredAmount, 0));
}
