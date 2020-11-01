import unittest
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned = 0
        for idx, ts in enumerate(timeSeries):
            if idx == len(timeSeries) - 1:
                poisoned += duration
                return poisoned
            if ts + duration - 1 < timeSeries[idx + 1]:
                poisoned += duration
            else:
                poisoned += timeSeries[idx + 1] - ts
        return poisoned


class Test(unittest.TestCase):
    def test_findPoisonedDuration(self):
        solution = Solution()
        self.assertEqual(solution.findPoisonedDuration([1, 4], 2), 4)
        self.assertEqual(solution.findPoisonedDuration([1, 2], 2), 3)


if __name__ == '__main__':
    unittest.main()
