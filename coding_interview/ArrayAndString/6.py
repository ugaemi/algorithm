import unittest


def compression_string(string):
    """
    문자열 압축
    :param string: 문자열
    :return: 압축한 문자열이 본래 문자열보다 길면 본래 문자열을, 아니면 압축한 문자열 리턴
    """
    compressed_string = string[0]
    count = 1
    for s in string[1:]:
        if compressed_string[-1] == s:
            count += 1
        else:
            compressed_string += str(count) + s
            count = 1
        if len(compressed_string) > len(string):
            return string
    compressed_string += str(count)
    return compressed_string


class Test(unittest.TestCase):
    def test_compression_string(self):
        self.assertEqual(compression_string('aabccccaaa'), 'a2b1c4a3')
        self.assertEqual(compression_string('abcabcabc'), 'abcabcabc')


if __name__ == '__main__':
    unittest.main()
