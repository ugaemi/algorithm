import unittest
from collections import deque


class Solution:
    def jaden_case(self, s: str) -> str:
        is_blank = True
        s = list(s)
        for i, c in enumerate(s):
            if c.isspace():
                is_blank = True
                continue
            elif c.isalpha():
                if is_blank:
                    s[i] = c.upper()
                else:
                    s[i] = c.lower()
            is_blank = False
        return "".join(s)

    def check_bracket(self, s: str) -> int:
        def check(s: deque):
            stack = []
            for c in s:
                if c == "(" or c == "{" or c == "[":
                    stack.append(c)
                else:
                    if not stack:
                        return False
                    x = stack.pop()
                    if c == ")" and x != "(":
                        return False
                    elif c == ")" and x != "(":
                        return False
                    elif c == "}" and x != "{":
                        return False
            return len(stack) == 0

        s = deque(s)
        answer = 0
        for x in range(len(s)):
            s.rotate(-1)
            if check(s):
                answer += 1
        return answer


class Test(unittest.TestCase):
    def test_jaden_case(self):
        solution = Solution()
        self.assertEqual(solution.jaden_case("3people unFollowed me"), "3people Unfollowed Me")
        self.assertEqual(solution.jaden_case("for the last week"), "For The Last Week")

    def test_check_bracket(self):
        solution = Solution()
        self.assertEqual(solution.check_bracket("[](){}"), 3)
        self.assertEqual(solution.check_bracket("}]()[{"), 2)
        self.assertEqual(solution.check_bracket("[)(]"), 0)
        self.assertEqual(solution.check_bracket("}}}"), 0)


if __name__ == "__main__":
    unittest.main()
