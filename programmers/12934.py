import math
import unittest


def is_sqrt(n):
    return (math.sqrt(n)+1)**2 if str(math.sqrt(n)).split('.')[-1] == '0' else -1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sqrt(121), 144)
        self.assertEqual(is_sqrt(3), -1)


if __name__ == '__main__':
    unittest.main()
