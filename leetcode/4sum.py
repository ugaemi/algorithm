import unittest
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int):
        res = []
        nums.sort()
        length = len(nums)

        for i in range(length - 3):
            if nums[i] > target:
                break
            for j in range(i+1, length - 2):
                if j > target and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, length - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return list(set(res))


class Test(unittest.TestCase):
    def test_threeSumClosest(self):
        solution = Solution()
        self.assertEqual(solution.fourSum([1, 0, -1, 0, -2, 2], 0),
                         [[-1,  0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2]])
        self.assertEqual(solution.fourSum([0, 0, 0, 0], 0), [[0, 0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
