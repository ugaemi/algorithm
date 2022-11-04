import sys
import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


class Test(unittest.TestCase):
    def test_maxProfit(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(solution.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
