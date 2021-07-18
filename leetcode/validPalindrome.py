import re
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


class Test(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(solution.isPalindrome("race a car"), False)


if __name__ == '__main__':
    unittest.main()
