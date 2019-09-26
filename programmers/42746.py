import unittest


def big_num(numbers):
    for n in numbers[:]:
        print(str(n)[0])
    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_num([6, 10, 2]), "6210")
        self.assertEqual(big_num([3, 30, 34, 5, 9]), "9534330")


if __name__ == '__main__':
    unittest.main()
