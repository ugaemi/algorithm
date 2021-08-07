import unittest


def num_array(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    return sorted(answer) if answer else [-1]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(num_array([5, 9, 7, 10], 5), [5, 10])
        self.assertEqual(num_array([2, 36, 1, 3], 1), [1, 2, 3, 36])
        self.assertEqual(num_array([3, 2, 6], 10), [-1])


if __name__ == '__main__':
    unittest.main()
