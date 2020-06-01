from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even += 1
        return even
