import collections
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[0][0]
