"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""
import unittest


class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x


class Test(unittest.TestCase):
    def test_fib(self):
        solution = Solution()
        self.assertEqual(solution.fib(2), 1)
        self.assertEqual(solution.fib(3), 2)
        self.assertEqual(solution.fib(4), 3)


if __name__ == "__main__":
    unittest.main()
