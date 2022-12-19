import unittest
from collections import Counter


def solution(topping):
    answer = 0
    c = Counter(topping)
    s = set()
    for i in topping:
        c[i] -= 1
        s.add(i)
        if c[i] == 0:
            c.pop(i)
        if len(c) == len(s):
            answer += 1
    return answer


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2, solution([1, 2, 1, 3, 1, 4, 1, 2]))
        self.assertEqual(0, solution([1, 2, 3, 1, 4]))


if __name__ == "__main__":
    unittest.main()
