from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([a*a for a in A])
