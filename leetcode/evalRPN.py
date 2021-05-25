import unittest
from math import trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(trunc(a / b))
        return stack[0]


class Test(unittest.TestCase):
    def test_evalRPN(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(solution.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)


if __name__ == '__main__':
    unittest.main()
