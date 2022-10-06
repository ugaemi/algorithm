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

    def get(self, key: str, timestamp: int) -> str:
        for i, (ts, v) in enumerate(sorted(self.dict[key].items(), reverse=True)):
            if ts <= timestamp:
                return self.dict[key][ts]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class Test(unittest.TestCase):
    def test_TimeMap(self):
        obj = TimeMap()
        obj.set("foo", "bar", 1)
        self.assertEqual(obj.get("foo", 1), "bar")


if __name__ == "__main__":
    unittest.main()
