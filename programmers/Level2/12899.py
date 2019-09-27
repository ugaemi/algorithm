import math
import unittest


def check_zero(n):
    if not n:
        return '4'
    return str(n)


def country_124(n):
    answer = []
    if n <= 2:
        return str(n)
    else:
        while n > 2:
            answer.append(check_zero(n % 3))
            if not n % 3:
                n = math.floor(n / 3) - 1
            else:
                n = math.floor(n / 3)
        answer.append(str(n))
    return str(int(''.join(answer[::-1])))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(country_124(1), '1')
        self.assertEqual(country_124(2), '2')
        self.assertEqual(country_124(3), '4')
        self.assertEqual(country_124(4), '11')
        self.assertEqual(country_124(5), '12')
        self.assertEqual(country_124(6), '14')
        self.assertEqual(country_124(7), '21')
        self.assertEqual(country_124(8), '22')
        self.assertEqual(country_124(9), '24')
        self.assertEqual(country_124(10), '41')


if __name__ == '__main__':
    unittest.main()
