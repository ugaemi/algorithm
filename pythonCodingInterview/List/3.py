import unittest


def remove_center_number(numbers):
    """
    리스트의 가운데 원소 삭제
    :param numbers: 리스트
    :return: 가운데 원소가 삭제된 리스트
    """
    if type(len(numbers)/2) == float:
        numbers.pop(len(numbers)//2)
    return numbers


class Test(unittest.TestCase):
    def test_remove_center_number(self):
        self.assertEqual(remove_center_number([3, 1, 5, 2, 4, 2, 1]), [3, 1, 5, 4, 2, 1])


if __name__ == '__main__':
    unittest.main()
