import unittest


def simpleArraySum(ar):
    return sum(ar)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(simpleArraySum([1, 2, 3, 4, 10, 11]), 31)


if __name__ == '__main__':
    unittest.main()
