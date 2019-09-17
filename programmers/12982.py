import unittest


def budget(d, bg):
    max_d = 0
    for i, v in enumerate(sorted(d)):
        max_d += v
        if max_d > bg:
            return i
    return len(d)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(budget([1, 3, 2, 5, 4], 9), 3)
        self.assertEqual(budget([2, 2, 3, 3], 10), 4)


if __name__ == '__main__':
    unittest.main()
