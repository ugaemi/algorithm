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
