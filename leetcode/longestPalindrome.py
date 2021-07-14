import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


class Test(unittest.TestCase):
    def test_longestPalindrome(self):
        solution = Solution()
        self.assertCountEqual(solution.longestPalindrome("babad"), "bab")
        self.assertCountEqual(solution.longestPalindrome("cbbd"), "bb")
        self.assertCountEqual(solution.longestPalindrome("a"), "a")
        self.assertCountEqual(solution.longestPalindrome("ac"), "a")


if __name__ == '__main__':
    unittest.main()
