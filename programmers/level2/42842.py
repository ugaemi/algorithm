import math
import unittest
from typing import List


def carpet(brown: int, yellow: int) -> List[int]:
    for yellow_w in range(int(math.sqrt(yellow)), yellow + 1):
        yellow_h = int(yellow / yellow_w)
        if yellow_h > yellow_w:
            continue
        if brown == (yellow_w + 2) * (yellow_h + 2) - yellow:
            return [yellow_w + 2, yellow_h + 2]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(carpet(10, 2), [4, 3])
        self.assertEqual(carpet(8, 1), [3, 3])
        self.assertEqual(carpet(24, 24), [8, 6])


if __name__ == "__main__":
    unittest.main()
