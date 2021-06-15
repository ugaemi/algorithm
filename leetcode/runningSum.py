import unittest


class Solution:
    def runningSum(self, nums):
        i = 1
        while i < len(nums):
            nums[i] += nums[i - 1]
            i += 1
        return nums


class Test(unittest.TestCase):
    def test_addStrings(self):
        solution = Solution()
        self.assertEqual(solution.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])
        self.assertEqual(solution.runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(solution.runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])


if __name__ == '__main__':
    unittest.main()
