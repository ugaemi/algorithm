import unittest
from typing import List


def h_index(citations: List[int]) -> int:
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(h_index([3, 0, 6, 1, 5]), 3)


if __name__ == "__main__":
    unittest.main()
