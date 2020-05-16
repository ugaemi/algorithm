from typing import List

import unittest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        if height[start] < height[end]:
            min_height = height[start]
            area = min_height * (end - start)
            start += 1
        else:
            min_height = height[end]
            area = min_height * (end - start)
            end -= 1

        while start != end:
            if height[end] > height[start]:
                tmp_min_height = height[start]
                tmp_area = tmp_min_height * (end - start)
                if tmp_area > area:
                    area = tmp_area
                start += 1
            else:
                tmp_min_height = height[end]
                tmp_area = tmp_min_height * (end - start)
                if tmp_area > area:
                    area = tmp_area
                end -= 1
        return area


class Test(unittest.TestCase):
    def test_maxArea(self):
        solution = Solution()
        self.assertEqual(solution.maxArea([1, 1]), 1)
        self.assertEqual(solution.maxArea([2, 3, 4, 5, 18, 17, 6]), 17)
        self.assertEqual(solution.maxArea([1, 3, 2, 5, 25, 24, 5]), 24)
        self.assertEqual(solution.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 25)


if __name__ == '__main__':
    unittest.main()
