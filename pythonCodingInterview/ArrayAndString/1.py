import unittest


def check_same_s_in_string(string):
    """
    문자열에 같은 문자가 중복되어 등장하는지 확인
    :param string: 문자열
    :return: 같은 문자가 있으면 True, 없으면 False
    """
    for s in string:
        if string.count(s) > 1:
            return True
        return False


class Test(unittest.TestCase):
    def test_check_same_str(self):
        self.assertEqual(check_same_s_in_string('stringstr'), True)
        self.assertEqual(check_same_s_in_string('string'), False)


if __name__ == '__main__':
    unittest.main()
