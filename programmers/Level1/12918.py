import unittest


def care_str(s):
    if len(s) in [4, 6]:
        try:
            int(s)
            return True
        except:
            return False
    return False


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(care_str('a234'), False)
        self.assertEqual(care_str('1234'), True)


if __name__ == '__main__':
    unittest.main()
