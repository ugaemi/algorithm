import unittest


def check_permutation(a, b):
    """
    두 문자열이 서로 순열 관계인지 확인
    :param a: 첫 번째 문자열
    :param b: 두 번째 문자열
    :return: 순열 관계라면 True, 아니면 False
    """
    if len(a) != len(b):
        return False
    return True if sorted(a) == sorted(b) else False


class Test(unittest.TestCase):
    def test_check_permutation(self):
        self.assertEqual(check_permutation('string', 'grtnsi'), True)
        self.assertEqual(check_permutation('string', 'str'), False)
        self.assertEqual(check_permutation('string', 'gngnst'), False)


if __name__ == '__main__':
    unittest.main()
