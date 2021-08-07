import unittest


def find_prime(n):
    a = set([i for i in range(3, n+1, 2)])
    for i in range(3, n+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, n+1, i)])
    return len(a) + 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_prime(10), 4)
        self.assertEqual(find_prime(5), 3)


if __name__ == '__main__':
    unittest.main()
