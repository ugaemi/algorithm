import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())


class Test(unittest.TestCase):
    def test_reverseWords(self):
        solution = Solution()
        self.assertEqual(solution.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
        self.assertEqual(solution.reverseWords("God Ding"), "doG gniD")


if __name__ == '__main__':
    unittest.main()
