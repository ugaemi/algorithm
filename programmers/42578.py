"""
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.
"""
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
