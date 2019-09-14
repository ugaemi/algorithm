import unittest


def collatz(num):
    if num == 1:
        return 0
    for i in range(1, 501):
        num = num / 2 if not num % 2 else num * 3 + 1
        if num == 1:
            return i
    return -1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(collatz(6), 8)
        self.assertEqual(collatz(16), 4)
        self.assertEqual(collatz(626331), -1)


if __name__ == '__main__':
    unittest.main()
