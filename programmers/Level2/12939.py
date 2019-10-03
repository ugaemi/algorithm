import unittest


def max_and_min(s):
    num_list = sorted(list(map(int, s.split(' '))))
    return str(num_list[0]) + ' ' + str(num_list[-1])


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_and_min("1 2 3 4"), "1 4")
        self.assertEqual(max_and_min("-1 -2 -3 -4"), "-4 -1")
        self.assertEqual(max_and_min("-1 -1"), "-1 -1")


if __name__ == '__main__':
    unittest.main()
