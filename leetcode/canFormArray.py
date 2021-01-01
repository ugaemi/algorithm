import unittest


class Solution:
    def canFormArray(self, arr, pieces):
        for piece in pieces:
            if len(piece) > 1:
                result = any(piece == arr[i:i+len(piece)] for i in range(len(arr) - 1))
                if not result:
                    return result
            else:
                if piece[0] not in arr:
                    return False
        return True


class Test(unittest.TestCase):
    def test_canFormArray(self):
        solution = Solution()
        self.assertEqual(solution.canFormArray([85], [[85]]), True)
        self.assertEqual(solution.canFormArray([15, 88], [[88], [15]]), True)
        self.assertEqual(solution.canFormArray([49, 18, 16], [[16, 18, 49]]), False)
        self.assertEqual(solution.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]), True)
        self.assertEqual(solution.canFormArray([1, 3, 5, 7], [[2, 4, 6, 8]]), False)


if __name__ == '__main__':
    unittest.main()
