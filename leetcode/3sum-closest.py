import unittest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[0:3])
        d = abs(target - res)
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total
                total_d = abs(total - target)
                if total_d < d:
                    res, d = total, total_d
                if total < target:
                    j += 1
                else:
                    k -= 1
        return res


class Test(unittest.TestCase):
    def test_threeSumClosest(self):
        solution = Solution()
        self.assertEqual(solution.threeSumClosest([-1, 2, 1, -4], 1), 2)


if __name__ == '__main__':
    unittest.main()
