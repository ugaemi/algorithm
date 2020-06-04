import unittest
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        Acost = []
        Bcost = []
        plain = []
        for cost in costs:
            plain.append(cost[0])
            plain.append(cost[1])
        plain.sort()
        for num in plain:
            print(Acost, Bcost)
            i = 0
            while costs:
                print(i)
                if num in costs[i]:
                    if costs[i].index(num) == 0:
                        Acost.append(num)
                    else:
                        Bcost.append(num)
                    del costs[i]
                    break
                i += 1
        return sum(Acost) + sum(Bcost)


class Test(unittest.TestCase):
    def test_twoCitySchedCost(self):
        solution = Solution()
        self.assertEqual(solution.twoCitySchedCost(
            [[10, 20], [30, 200], [400, 50], [30, 20]]), 110)
        self.assertEqual(solution.twoCitySchedCost(
            [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]), 1859)


if __name__ == '__main__':
    unittest.main()
