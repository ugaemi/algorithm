import unittest


class Solution:
    PARENTHESES = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    def is_valid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c not in self.PARENTHESES:
                stack.append(c)
            else:
                if not stack or stack.pop() != self.PARENTHESES[c]:
                    return False
        return len(stack) == 0


class Test(unittest.TestCase):
    def test_is_valid(self):
        solution = Solution()
        self.assertEqual(solution.is_valid("()"), True)
        self.assertEqual(solution.is_valid("()[]{}"), True)
        self.assertEqual(solution.is_valid("(}"), False)
        self.assertEqual(solution.is_valid("["), False)
        self.assertEqual(solution.is_valid("]"), False)


if __name__ == "__main__":
    unittest.main()
