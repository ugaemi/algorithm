import unittest


class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


class Test(unittest.TestCase):
    def test_arrayPairSum(self):
        solution = Solution()
        self.assertEqual(solution.arrayPairSum([1, 4, 3, 2]), 4)
        self.assertEqual(solution.arrayPairSum([6, 2, 6, 5, 1, 2]), 9)


if __name__ == '__main__':
    unittest.main()
