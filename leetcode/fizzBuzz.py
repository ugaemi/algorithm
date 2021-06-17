import unittest
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if i % 15 == 0 else 'Buzz' if i % 5 == 0 else 'Fizz' if i % 3 == 0 else str(i) for i in range(1, n+1)]


class Test(unittest.TestCase):
    def test_majorityElement(self):
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(3), ["1", "2", "Fizz"])
        self.assertEqual(solution.fizzBuzz(5), ["1","2","Fizz","4","Buzz"])
        self.assertEqual(solution.fizzBuzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])


if __name__ == '__main__':
    unittest.main()
