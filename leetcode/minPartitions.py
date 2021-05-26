import unittest


class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(d) for d in n])


class Test(unittest.TestCase):
    def test_minPartitions(self):
        solution = Solution()
        self.assertEqual(solution.minPartitions("32"), 3)
        self.assertEqual(solution.minPartitions("82734"), 8)
        self.assertEqual(solution.minPartitions("27346209830709182346"), 9)


if __name__ == '__main__':
    unittest.main()
