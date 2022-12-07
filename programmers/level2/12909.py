import unittest


def valid_parenthesis(s: str) -> bool:
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    if stack:
        return False
    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(valid_parenthesis("()()"), True)
        self.assertEqual(valid_parenthesis("(())()"), True)
        self.assertEqual(valid_parenthesis(")()("), False)
        self.assertEqual(valid_parenthesis("(()("), False)


if __name__ == "__main__":
    unittest.main()
