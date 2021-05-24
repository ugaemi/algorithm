import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class Test(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(121), True)
        self.assertEqual(solution.isPalindrome(-121), False)
        self.assertEqual(solution.isPalindrome(10), False)
        self.assertEqual(solution.isPalindrome(-101), False)


if __name__ == '__main__':
    unittest.main()
