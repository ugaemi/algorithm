import unittest
from typing import List


def min_rectangle(sizes: List[List[int]]) -> int:
    max_w, max_h = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        max_w, max_h = max(max_w, w), max(max_h, h)
    return max_w * max_h


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_rectangle([[60, 50], [30, 70], [60, 30], [80, 40]]), 4000)
        self.assertEqual(min_rectangle([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]), 120)
        self.assertEqual(min_rectangle([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]), 133)


if __name__ == "__main__":
    unittest.main()
