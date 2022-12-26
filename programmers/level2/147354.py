from functools import reduce

import unittest


def solution(data, col, row_begin, row_end):
    result = []
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin - 1, row_end):
        s = 0
        for n in data[i]:
            s += n % (i + 1)
        result.append(s)
    return reduce(lambda x, y: x ^ y, result)


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3), 4)
        self.assertEqual(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3), 4)


if __name__ == "__main__":
    unittest.main()
