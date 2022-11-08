"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
"""
import unittest
from collections import defaultdict

from typing import List


def best_album(genres: List[str], plays: List[int]) -> List[int]:
    album = []
    play_dict, total_dict = defaultdict(list), defaultdict(int)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        play_dict[genre].append((i, play))
        total_dict[genre] += play
    for (k, v) in sorted(total_dict.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(play_dict[k], key=lambda x: x[1], reverse=True)[:2]:
            album.append(i)
    return album


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(
            best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]), [4, 1, 3, 0]
        )


if __name__ == "__main__":
    unittest.main()
