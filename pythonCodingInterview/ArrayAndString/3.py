import unittest


def url_encoder(string):
    """
    문자열에 들어있는 모든 공백을 '%20'으로 바꿈
    :param string: 문자열
    :return: 공백이 %20으로 바뀐 문자열
    """
    return string.replace(' ', '%20')


class Test(unittest.TestCase):
    def test_url_encoder(self):
        self.assertEqual(url_encoder('Mr John Smith'), 'Mr%20John%20Smith')


if __name__ == '__main__':
    unittest.main()
