# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.stack = []

    def getDecimalValue(self, head: ListNode) -> int:
        self.stack.append(head.val)
        if head.next:
            return self.getDecimalValue(head.next)
        i = 0
        result = 0
        while len(self.stack):
            val = self.stack.pop()
            if val == 1:
                result += 2 ** i
            i += 1
        return result
