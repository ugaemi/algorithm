import collections
import re
import unittest
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pure_paragraph = re.sub("[^\w]", " ", paragraph.lower())
        words = pure_paragraph.split()
        no_banned_paragraphs = []
        for word in words:
            if not word or word in banned:
                continue
            no_banned_paragraphs.append(word)
        counter = collections.Counter(no_banned_paragraphs)
        return counter.most_common()[0][0]


class Test(unittest.TestCase):
    def test_mostCommonWord(self):
        solution = Solution()
        self.assertEqual(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]), "ball")
        self.assertEqual(solution.mostCommonWord("a.", []), "a")


if __name__ == '__main__':
    unittest.main()
