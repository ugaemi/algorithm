"""
문제 1.
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

문제 2.
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

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
