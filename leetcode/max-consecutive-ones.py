from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        oneCount = 0
        for num in nums:
            if num == 1:
                oneCount += 1
            else:
                if maxNum < oneCount:
                    maxNum = oneCount
                oneCount = 0
        return maxNum if maxNum > oneCount else oneCount
