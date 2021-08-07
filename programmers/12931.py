import unittest
from functools import reduce


def sum_digit(n):
    return reduce(lambda x, y: x + y, list(map(int, list(str(n)))))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digit(123), 6)
        self.assertEqual(sum_digit(987), 24)


if __name__ == '__main__':
    unittest.main()
