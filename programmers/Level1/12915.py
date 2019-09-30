import unittest


def sort_my_strings(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_my_strings(["sun", "bed", "car"], 1), ["car", "bed", "sun"])
        self.assertEqual(sort_my_strings(["abce", "abcd", "cdx"], 2), ["abcd", "abce", "cdx"])


if __name__ == '__main__':
    unittest.main()
