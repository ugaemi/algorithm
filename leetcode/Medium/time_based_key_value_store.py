"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""
import unittest
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.dict = defaultdict(defaultdict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key][timestamp] = value

    def search(self, key: str, timestamp: int):
        sorted_keys = sorted(list(self.dict[key].keys()))
        start, end = 0, len(sorted_keys)
        if timestamp < sorted_keys[0]:
            return ""
        mid = 0
        while start < end:
            mid = (start + end) // 2
            if sorted_keys[mid] < timestamp:
                start = mid + 1
            elif sorted_keys[mid] > timestamp:
                end = mid
            else:
                break
        return self.dict[key].get(sorted_keys[mid], "")

    def get(self, key: str, timestamp: int) -> str:
        return self.dict[key].get(timestamp, self.search(key, timestamp))


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TimeMapTest(unittest.TestCase):
    def test_TimeMap1(self):
        obj = TimeMap()
        self.assertIsNone(obj.set("foo", "bar", 1))
        self.assertEqual(obj.get("foo", 1), "bar")
        self.assertEqual(obj.get("foo", 3), "bar")
        self.assertIsNone(obj.set("foo", "bar2", 4))
        self.assertEqual(obj.get("foo", 4), "bar2")
        self.assertEqual(obj.get("foo", 5), "bar2")

    def test_TimeMap2(self):
        obj = TimeMap()
        self.assertIsNone(obj.set("love", "high", 10))
        self.assertIsNone(obj.set("love", "low", 20))
        self.assertEqual(obj.get("love", 5), "")
        self.assertEqual(obj.get("love", 10), "high")
        self.assertEqual(obj.get("love", 15), "high")
        self.assertEqual(obj.get("love", 20), "low")
        self.assertEqual(obj.get("love", 25), "low")


if __name__ == "__main__":
    unittest.main()
