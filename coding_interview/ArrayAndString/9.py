import unittest


def rotation_string(s1, s2):
    """
    s2가 s1을 회전시킨 결과인지 판별
    :param s1: 첫 번째 문자열
    :param s2: 두 번째 문자열
    :return: 회전시킨게 맞다면 True, 아니면 False
    """
    if s2 in s1 + s1:
        return True
    return False


class Test(unittest.TestCase):
    def test_rotation_string(self):
        self.assertEqual(rotation_string('waterbottle', 'erbottlewat'), True)
        self.assertEqual(rotation_string('birthday', 'thdayybirt'), False)


if __name__ == '__main__':
    unittest.main()
