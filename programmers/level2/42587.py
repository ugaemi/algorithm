import unittest
from collections import deque


def printer(priorities, location) -> int:
    answer = 0
    dq = deque([(v, i) for i, v in enumerate(priorities)])
    while dq:
        item = dq.popleft()
        if dq and max(dq)[0] > item[0]:
            dq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(printer([2, 1, 3, 2], 2), 1)
        self.assertEqual(printer([1, 1, 9, 1, 1, 1], 0), 5)


if __name__ == "__main__":
    unittest.main()
