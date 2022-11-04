"""
nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.
"""
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
