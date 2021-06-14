import unittest

from collections import Counter


def palindrome_permutation(string):
    """
    문자열이 회문의 순열인지 아닌지 확인
    :param string: 문자열
    :return: 회문의 순열이면 True, 아니면 False
    """
    odd_count = 0
    string = ''.join(string.lower().split())
    string_set = Counter(string).most_common()
    for s in string_set:
        if s[1] % 2:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


class Test(unittest.TestCase):
    def test_palindrome_permutation(self):
        self.assertEqual(palindrome_permutation('Tact Coa'), True)
        self.assertEqual(palindrome_permutation('AA Abb'), True)


if __name__ == '__main__':
    unittest.main()
