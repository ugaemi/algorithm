import unittest


class Solution:
    def maxPower(self, s: str) -> int:
        count = maxCount = 1
        last = s[0]
        for c in s[1:]:
            if c == last:
                count += 1
            maxCount = max(count, maxCount)
            if c != last:
                count = 1
                last = c
        return maxCount


class Test(unittest.TestCase):
    def test_maxArea(self):
        solution = Solution()
        self.assertEqual(solution.maxPower('leetcode'), 2)
        self.assertEqual(solution.maxPower('abbcccddddeeeeedcba'), 5)
        self.assertEqual(solution.maxPower('triplepillooooow'), 5)
        self.assertEqual(solution.maxPower('hooraaaaaaaaaaay'), 11)
        self.assertEqual(solution.maxPower('cc'), 2)


if __name__ == '__main__':
    unittest.main()


# class Solution:
#     def maxPower(self, s: str) -> int:
#          return max(len(list(j)) for _,j in groupby(s))
