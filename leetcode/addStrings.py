import unittest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


class Test(unittest.TestCase):
    def test_addStrings(self):
        solution = Solution()
        self.assertEqual(solution.addStrings("11", "123"), "134")
        self.assertEqual(solution.addStrings("456", "77"), "533")
        self.assertEqual(solution.addStrings("0", "0"), "0")


if __name__ == '__main__':
    unittest.main()
