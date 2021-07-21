import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= p
            p *= nums[i]
        return out


class Test(unittest.TestCase):
    def test_productExceptSelf(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


if __name__ == '__main__':
    unittest.main()
