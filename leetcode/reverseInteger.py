import unittest


class Solution:
    def reverse(self, x: int) -> int:
        result = -int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        if -2**31 <= result <= (2**31)-1:
            return result
        return 0


class Test(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(120), 21)
        self.assertEqual(solution.reverse(0), 0)


if __name__ == '__main__':
    unittest.main()
