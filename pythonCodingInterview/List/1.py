import unittest


def remove_duplication(numbers):
    """
    리스트에서 중복되는 원소 삭제
    :param numbers: 리스트
    :return: 중복되는 원소가 삭제된 리스트
    """
    result = []
    for n in numbers:
        if n not in result:
            result.append(n)
    return result


class Test(unittest.TestCase):
    def test_remove_duplication(self):
        self.assertEqual(remove_duplication([3, 1, 5, 2, 4, 2, 2, 1]), [3, 1, 5, 2, 4])


if __name__ == '__main__':
    unittest.main()
