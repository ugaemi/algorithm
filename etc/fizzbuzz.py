import unittest


def fb(n):
    answer = ''
    if not n % 3 or not n % 5:
        if not n % 3:
            answer += 'fizz'
        if not n % 5:
            answer += 'buzz'
        return answer
    return n


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(fb(1), 1)
        self.assertEqual(fb(3), 'fizz')
        self.assertEqual(fb(5), 'buzz')
        self.assertEqual(fb(15), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()
