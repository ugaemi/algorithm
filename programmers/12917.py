import unittest


def descending_order(s):
    return ''.join(sorted(s, reverse=True))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(descending_order("Zbcdefg"), "gfedcbZ")


if __name__ == '__main__':
    unittest.main()
