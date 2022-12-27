import unittest
import heapq


def solution(n, k, enemy):
    h = []
    total, answer = 0, 0
    for e in enemy:
        total += e
        if total <= n:
            heapq.heappush(h, -e)
            answer += 1
        elif k > 0:
            k -= 1
            total += heapq.heappushpop(h, -e)
            answer += 1
        else:
            break
    return answer


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]), 5)
        self.assertEqual(solution(2, 4, [3, 3, 3, 3]), 4)


if __name__ == "__main__":
    unittest.main()
