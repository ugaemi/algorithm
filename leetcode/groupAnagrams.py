import collections
import unittest
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())


class Test(unittest.TestCase):
    def test_groupAnagrams(self):
        solution = Solution()
        self.assertCountEqual(
            solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
        self.assertCountEqual(solution.groupAnagrams([""]), [[""]])
        self.assertCountEqual(solution.groupAnagrams(["a"]), [["a"]])


if __name__ == '__main__':
    unittest.main()
