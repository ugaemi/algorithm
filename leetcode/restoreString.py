import unittest
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(i for i in res)


class Test(unittest.TestCase):
    def test_restoreString(self):
        solution = Solution()
        self.assertEqual(solution.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), "leetcode")
        self.assertEqual(solution.restoreString("abc", [0, 1, 2]), "abc")
        self.assertEqual(solution.restoreString("aiohn", [3, 1, 4, 2, 0]), "nihao")


if __name__ == '__main__':
    unittest.main()
