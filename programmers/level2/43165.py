import unittest
from typing import List


def target_number(numbers: List[int], target: int) -> int:
    answer = 0
    queue = [[numbers[0], 0], [-1 * numbers[0], 0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(target_number([1, 1, 1, 1, 1], 3), 5)
        self.assertEqual(target_number([4, 1, 2, 1], 4), 2)


if __name__ == "__main__":
    unittest.main()
