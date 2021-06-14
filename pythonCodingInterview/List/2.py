import unittest


def get_number(numbers, i):
    """
    뒤에서 i번째 원소 구함
    :param numbers: 리스트
    :param i: 인덱스
    :return: 뒤에서 i번째 원소 리턴
    """
    return numbers[-i]


class Test(unittest.TestCase):
    def test_get_number(self):
        self.assertEqual(get_number([3, 1, 5, 2, 4, 2, 2, 1], 3), 2)


if __name__ == '__main__':
    unittest.main()
