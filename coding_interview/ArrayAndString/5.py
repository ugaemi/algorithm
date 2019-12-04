import unittest


def one_edit_replace(s1, s2):
    """
    한 번 이상 교체하는지 확인
    :param s1: 첫 번째 문자열
    :param s2: 두 번째 문자열
    :return: 한 번 이상 교체하면 False, 아니면 True
    """
    found_difference = False
    for i, v in enumerate(s1):
        if v != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_edit_insert(s1, s2):
    """
    한 번 이상 삽입하거나 삭제하는지 확인
    :param s1: 첫 번째 문자열
    :param s2: 두 번째 문자열
    :return: 한 번 이상 삽입하거나 삭제하면 False, 아니면 True
    """
    index1 = 0
    index2 = 0
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def one_edit_away(first, second):
    """
    두 문자열의 길이 비교
    :param first: 첫 번째 문자열
    :param second: 두 번째 문자열
    :return: 같으면 one_edit_replace, 다르면 one_edit_insert
    """
    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif len(first) + 1 == len(second):
        return one_edit_insert(first, second)
    elif len(first) - 1 == len(second):
        return one_edit_insert(second, first)
    return False


class Test(unittest.TestCase):
    def test_one_edit_away(self):
        self.assertEqual(one_edit_away('pale', 'ple'), True)
        self.assertEqual(one_edit_away('pales', 'pale'), True)
        self.assertEqual(one_edit_away('pale', 'bale'), True)
        self.assertEqual(one_edit_away('pale', 'bake'), False)


if __name__ == '__main__':
    unittest.main()
