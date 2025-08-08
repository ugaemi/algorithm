def isBalanced(s):
    # Dictionary to hold matching pairs of brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_pairs.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_pairs.keys():  # If it's a closing bracket
            if not stack or stack[-1] != bracket_pairs[char]:
                return "NO"  # Unmatched closing bracket
            stack.pop()  # Matched, pop the last opening bracket

    return "YES" if not stack else "NO"  # If stack is empty, all brackets matched
