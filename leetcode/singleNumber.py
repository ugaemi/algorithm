import collections
import unittest


class Solution:
    def singleNumber(self, nums):
        return collections.Counter(nums).most_common()[-1][0]


class Test(unittest.TestCase):
    def test_singleNumber(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([2, 2, 1]), 1)
        self.assertEqual(solution.singleNumber([4, 1, 2, 1, 2]), 4)


if __name__ == '__main__':
    unittest.main()
