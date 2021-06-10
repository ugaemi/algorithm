import unittest


class MyCalender:

    def __init__(self):
        self.head = {'start': -1, 'end': -1, 'next': {'start': float('inf'), 'end': float('inf')}}

    def book(self, start, end):
        curr = self.head
        while curr['start'] < start:
            last, curr = curr, curr['next']
        if last['end'] > start or curr['start'] < end:
            return False
        last['next'] = {'start': start, 'end': end, 'next': curr}
        return True


class Test(unittest.TestCase):
    def test_MyCalender(self):
        calendar = MyCalender()
        self.assertEqual(calendar.book(10, 20), True)
        self.assertEqual(calendar.book(15, 25), False)
        self.assertEqual(calendar.book(20, 30), True)


if __name__ == '__main__':
    unittest.main()
