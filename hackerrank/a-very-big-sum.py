import unittest


def aVeryBigSum(ar):
    return sum(ar)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]), 5000000015)


if __name__ == '__main__':
    unittest.main()
