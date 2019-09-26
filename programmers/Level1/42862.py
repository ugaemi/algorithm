import unittest


def gymsuit(n, lost, reserve):
    for r in reserve[:]:
        if r in lost:
            reserve.remove(r)
            lost.remove(r)
    for r in reserve:
        if not lost:
            break
        else:
            for l in lost:
                if abs(l-r) == 1:
                    lost.remove(l)
                    break
    return n - len(lost)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(gymsuit(5, [2, 4], [1, 3, 5]), 5)
        self.assertEqual(gymsuit(5, [2, 4], [3]), 4)
        self.assertEqual(gymsuit(3, [3], [1]), 2)
        self.assertEqual(gymsuit(8, [3, 4, 7], [1, 3, 5, 6]), 8)
        self.assertEqual(gymsuit(3, [1, 2], [2, 3]), 2)
        self.assertEqual(gymsuit(9, [2, 4, 7, 8], [3, 6, 9]), 8)
        self.assertEqual(gymsuit(5, [2, 4], [3, 5]), 5)


if __name__ == '__main__':
    unittest.main()
