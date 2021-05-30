import unittest


class Solution:
    def __init__(self):
        self.d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        for i in s[::-1]:
            if self.d[i] >= prev:
                res += self.d[i]
            else:
                res -= self.d[i]
            prev = self.d[i]
        return res


class Test(unittest.TestCase):
    def test_romanToInt(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("III"), 3)
        self.assertEqual(solution.romanToInt("IV"), 4)
        self.assertEqual(solution.romanToInt("IX"), 9)
        self.assertEqual(solution.romanToInt("LVIII"), 58)
        self.assertEqual(solution.romanToInt("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
