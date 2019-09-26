import unittest


def string_middle(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    return s[len(s)//2]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_middle('abced'), 'c')
        self.assertEqual(string_middle('qwer'), 'we')


if __name__ == '__main__':
    unittest.main()
