import unittest


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


class Test(unittest.TestCase):
    def test_defangIPaddr(self):
        solution = Solution()
        self.assertEqual(solution.defangIPaddr("1.1.1.1"), "1[.]1[.]1[.]1")
        self.assertEqual(solution.defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")


if __name__ == '__main__':
    unittest.main()
