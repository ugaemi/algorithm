import collections
import re
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

    # def isPalindrome(self, s: str) -> bool:
    #     deque = collections.deque()
    #     for c in s:
    #         if c.isalnum():
    #             deque.append(c.lower())
    #     while len(deque) > 1:
    #         if deque.popleft() != deque.pop():
    #             return False
    #     return True

    # def isPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     s = re.sub('[^a-z0-9]', '', s)
    #     return s == s[::-1]


class Test(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(solution.isPalindrome("race a car"), False)


if __name__ == '__main__':
    unittest.main()
