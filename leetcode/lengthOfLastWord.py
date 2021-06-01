import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            return len(s.split()[-1])
        except IndexError:
            return 0


class Test(unittest.TestCase):
    def test_lengthOfLastWord(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(solution.lengthOfLastWord(" "), 0)


if __name__ == '__main__':
    unittest.main()
