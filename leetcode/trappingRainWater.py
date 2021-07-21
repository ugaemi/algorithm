import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters
            stack.append(i)
        return volume


class Test(unittest.TestCase):
    def test_trap(self):
        solution = Solution()
        self.assertEqual(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(solution.trap([4, 2, 0, 3, 2, 5]), 9)


if __name__ == '__main__':
    unittest.main()
