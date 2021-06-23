import unittest


class Solution(object):
    def removeOuterParentheses(self, S):
        res = ''
        stack = []
        basket = ''
        for p in S:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()
            basket += p
            if not stack:
                res += basket[1:-1]
                basket = ''
        return res


class Test(unittest.TestCase):
    def test_removeOuterParentheses(self):
        solution = Solution()
        self.assertEqual(solution.removeOuterParentheses("(()())(())"), "()()()")
        self.assertEqual(solution.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())")
        self.assertEqual(solution.removeOuterParentheses("()()"), "")


if __name__ == '__main__':
    unittest.main()
