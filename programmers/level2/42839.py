import itertools
import unittest


def is_prime_number(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def find_prime_number(numbers):
    answers = set()
    all_numbers = []
    for i in range(1, len(numbers) + 1):
        all_numbers.extend(list(itertools.permutations(list(numbers), i)))
    for number in all_numbers:
        n = int("".join([str(n) for n in number]))
        if is_prime_number(n):
            answers.add(n)
    return len(answers)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_prime_number("17"), 3)
        self.assertEqual(find_prime_number("011"), 2)


if __name__ == "__main__":
    unittest.main()
