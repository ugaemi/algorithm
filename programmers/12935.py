import unittest


def remove_min(arr):
    if len(arr) == 0 or len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_min([4, 3, 2, 1]), [4, 3, 2])
        self.assertEqual(remove_min([10]), [-1])


if __name__ == '__main__':
    unittest.main()
