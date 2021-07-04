import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for c in s:
            if c.isalnum():
                stack.append(c.lower())
        while len(stack) > 1:
            if stack.pop(0) != stack.pop():
                return False
        return True


class Test(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(solution.isPalindrome("race a car"), False)


if __name__ == '__main__':
    unittest.main()
