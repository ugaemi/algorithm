import unittest


class Solution(object):
    def replaceDigits(self, s):
        res = []

        for i in range(len(s)):
            if i % 2 == 0:
                res.append(s[i])
            if i % 2 == 1:
                res.append(chr(ord(s[i - 1]) + int(s[i])))

        return ''.join(res)


class Test(unittest.TestCase):
    def test_replaceDigits(self):
        solution = Solution()
        self.assertEqual(solution.replaceDigits("a1c1e1"), "abcdef")
        self.assertEqual(solution.replaceDigits("a1b2c3d4e"), "abbdcfdhe")


if __name__ == '__main__':
    unittest.main()
