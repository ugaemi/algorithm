import unittest


def solution(s):
    pass


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution('aabbaccc'), 7)
        self.assertEqual(solution('ababcdcdababcdcd'), 9)
        self.assertEqual(solution('abcabcdede'), 8)
        self.assertEqual(solution('abcabcabcabcdededededede'), 14)
        self.assertEqual(solution('xababcdcdababcdcd'), 17)


if __name__ == '__main__':
    unittest.main()
