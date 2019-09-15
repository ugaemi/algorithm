import unittest


def term_by_x(x, n):
    answer = [x]
    for i in range(n - 1):
        answer.append(answer[-1] + x)
    return answer


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(term_by_x(2, 5), [2, 4, 6, 8, 10])
        self.assertEqual(term_by_x(4, 3), [4, 8, 12])
        self.assertEqual(term_by_x(-4, 2), [-4, -8])


if __name__ == '__main__':
    unittest.main()
