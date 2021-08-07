import unittest


def next_big_number(n):
    cnt_1 = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == cnt_1:
            return n


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_big_number(78), 83)
        self.assertEqual(next_big_number(15), 23)


if __name__ == '__main__':
    unittest.main()
