import unittest


def electronic_board(phrases, second):
    s = second % 28
    if s <= 14:
        return '_' * (14 - s) + phrases[0:s]
    return phrases[s-14:] + '_' * (s - 14)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(electronic_board('happy-birthday', 3), '___________hap')
        self.assertEqual(electronic_board('happy-birthday', 14), 'happy-birthday')
        self.assertEqual(electronic_board('happy-birthday', 17), 'py-birthday___')
        self.assertEqual(electronic_board('happy-birthday', 28), '______________')


if __name__ == '__main__':
    unittest.main()
