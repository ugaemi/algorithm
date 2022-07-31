"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
"""
import collections
import unittest


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


class Test(unittest.TestCase):
    def test_MyStack(self):
        my_stack = MyStack()
        my_stack.push(1)
        my_stack.push(2)
        self.assertEqual(my_stack.top(), 2)
        self.assertEqual(my_stack.pop(), 2)
        self.assertEqual(my_stack.empty(), False)


if __name__ == "__main__":
    unittest.main()
