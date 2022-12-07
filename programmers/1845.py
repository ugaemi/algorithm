import unittest

from typing import List


def poncketmon(nums: List[int]):
    max_count = len(nums) / 2
    return min(max_count, len(set(nums)))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(poncketmon([3, 1, 2, 3]), 2)
        self.assertEqual(poncketmon([3, 3, 3, 2, 2, 4]), 3)
        self.assertEqual(poncketmon([3, 3, 3, 2, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
