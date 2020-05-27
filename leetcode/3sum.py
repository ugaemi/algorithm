import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        if len(nums) < 3:
            return res
        for i in range(len(nums)):
            needs = 0 - nums[i]
            for j in range(i+1, len(nums)):
                need = needs - nums[j]
                tmp_nums = nums[:]
                tmp_nums.remove(nums[i])
                tmp_nums.remove(nums[j])
                if need in tmp_nums:
                    answer = [nums[i], nums[j], need]
                    if sorted(answer) not in res:
                        res.append(answer)
        return res


# Best example
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         length = len(nums)
#
#         for i in range(length - 2):
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             l, r = i + 1, length - 1
#             while l < r:
#                 total = nums[i] + nums[l] + nums[r]
#                 if total < 0:
#                     l += 1
#                 elif total > 0:
#                     r -= 1
#                 else:
#                     res.append([nums[i], nums[l], nums[r]])
#                     while l < r and nums[l] == nums[l + 1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r - 1]:
#                         r -= 1
#                     l += 1
#                     r -= 1
#         return res
