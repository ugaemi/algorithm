import unittest


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


class Test(unittest.TestCase):
    def test_toLowerCase(self):
        solution = Solution()
        self.assertEqual(solution.toLowerCase("Hello"), "hello")
        self.assertEqual(solution.toLowerCase("here"), "here")
        self.assertEqual(solution.toLowerCase("LOVELY"), "lovely")


if __name__ == '__main__':
    unittest.main()
