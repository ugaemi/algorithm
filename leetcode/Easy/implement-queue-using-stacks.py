import unittest


class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []


class Test(unittest.TestCase):
    def test_MyQueue(self):
        my_queue = MyQueue()
        my_queue.push(1)
        my_queue.push(2)
        self.assertEqual(my_queue.peek(), 1)
        self.assertEqual(my_queue.pop(), 1)
        self.assertEqual(my_queue.empty(), False)


if __name__ == "__main__":
    unittest.main()
