class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None

def process_queries(queries):
    queue = QueueUsingTwoStacks()
    results = []

    for query in queries:
        parts = query.split()
        q_type = int(parts[0])

        if q_type == 1:  # Enqueue
            value = int(parts[1])
            queue.enqueue(value)
        elif q_type == 2:  # Dequeue
            queue.dequeue()
        elif q_type == 3:  # Print front element
            results.append(queue.front())

    return results

if __name__ == '__main__':
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    q = int(data[0])  # Number of queries
    queries = data[1:q + 1]

    results = process_queries(queries)

    for result in results:
        print(result)
