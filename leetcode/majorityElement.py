import collections
import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]


class Test(unittest.TestCase):
    def test_majorityElement(self):
        solution = Solution()
        self.assertEqual(solution.majorityElement([3, 2, 3]), 3)
        self.assertEqual(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == '__main__':
    unittest.main()
