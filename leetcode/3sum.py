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
#         ans = set()
#         if len(nums) < 3:
#             return ans
#         if nums.count(0) >= 3:
#             ans.add((0,0,0))
#         nums_set = set(nums)
#         numMax, numMin = max(nums_set), min(nums_set)
#         if numMax <= 0 or numMin >= 0:
#             return ans
#         setP = set(num for num in nums_set if (num > 0 and num <= -2 * numMin))
#         setN = set(num for num in nums_set if (num < 0 and num >= -2 * numMax))
#         count = collections.Counter(nums)
#         for numP in setP:
#             for numN in setN:
#                 numD = -numP - numN
#                 if numD in nums_set:
#                     val = tuple(sorted([numD, numP, numN]))
#                     if val.count(numD) <= count[numD] and val.count(numP) <= count[numP] and val.count(numN) <= count[numN]:
#                         ans.add(val)
#         return ans
