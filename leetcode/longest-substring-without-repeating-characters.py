import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        tmp = ''
        for c in s:
            if c not in tmp:
                tmp += c
            else:
                if len(tmp) > res:
                    res = len(tmp)
                tmp = tmp[tmp.index(c)+1:] + c
        return res if res > len(tmp) else len(tmp)


class Test(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring(" "), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("aab"), 2)
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), 3)


if __name__ == '__main__':
    unittest.main()
