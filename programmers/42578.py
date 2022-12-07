import collections
import unittest
from functools import reduce

from typing import List


def camouflage(clothes: List[List[str]]):
    return reduce(lambda x, y: x * y, [a + 1 for a in collections.Counter([x[1] for x in clothes]).values()]) - 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(
            camouflage([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]), 5
        )
        self.assertEqual(camouflage([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]), 3)


if __name__ == "__main__":
    unittest.main()
