import unittest


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k)


class Test(unittest.TestCase):
    def test_reverseStr(self):
        solution = Solution()
        self.assertEqual(solution.reverseStr("abcdefg", 2), "bacdfeg")
        self.assertEqual(solution.reverseStr("abcd", 2), "bacd")


if __name__ == '__main__':
    unittest.main()
