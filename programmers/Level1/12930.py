import unittest


def make_strange_str(string):
    idx = 0
    answer = ''
    str_list = list(string)
    for s in str_list:
        if s == ' ':
            answer += s
            idx = 0
            continue
        if idx % 2:
            answer += s.lower()
        else:
            answer += s.upper()
        idx += 1
    return answer


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(make_strange_str('try hello world'), 'TrY HeLlO WoRlD')


if __name__ == '__main__':
    unittest.main()
