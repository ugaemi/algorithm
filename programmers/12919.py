import unittest


def findKim(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(findKim(['Jane', 'Kim']), '김서방은 1에 있다')


if __name__ == '__main__':
    unittest.main()
