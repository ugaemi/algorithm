import unittest


def set_desc(n):
    return int(''.join(
        [str(n) for n in sorted([int(num) for num in str(n)], reverse=True)]))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_desc(118372), 873211)


if __name__ == '__main__':
    unittest.main()
