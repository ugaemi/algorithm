import unittest
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


class Test(unittest.TestCase):
    def test_maximumWealth(self):
        solution = Solution()
        self.assertEqual(solution.maximumWealth([[1, 2, 3], [3, 2, 1]]), 6)
        self.assertEqual(solution.maximumWealth([[1, 5], [7, 3], [3, 5]]), 10)
        self.assertEqual(solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)


if __name__ == '__main__':
    unittest.main()
