import unittest


class Solution:
    def insufficient_amount(self, price, money, count):
        required_amount = sum(map(lambda x: x * price, range(1, count + 1)))
        return required_amount - money if required_amount > money else 0


class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.insufficient_amount(3, 20, 4), 10)


if __name__ == "__main__":
    unittest.main()
